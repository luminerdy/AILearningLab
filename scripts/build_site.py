"""Build the public learning site from the workshop Markdown sources."""
from pathlib import Path
import html
import re
import shutil
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.site-tools'))
import markdown

CONTENT = ROOT / 'site' / 'content'
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
PAGES = {
    'llm-basics.md': ('llm-basics.html', 'LLM basics', 'BEFORE YOU BEGIN'),
    'agentic-ai-learning-progression-updated.md': ('full-progression.html', 'Human learning progression', 'THE FULL LEARNING FRAMEWORK'),
    'workshop-student-workbook.md': ('workbook.html', 'Complete student workbook', 'WORKSHOP REFERENCE'),
    'learning-path.md': ('labs.html', 'Keep learning', 'AFTER THE WORKSHOP'),
    'workshop-facilitator-guide.md': ('instructors.html', 'Instructor guide', 'TEACH THE WORKSHOP'),
}
SEQUENCE = [
    ('llm-basics.html', 'Introduction — LLM Basics'),
    ('lab-1-ask.html', 'Lab 1 — Ask'),
    ('lab-2-check-adjust.html', 'Lab 2 — Check and Adjust'),
    ('lab-3-challenge.html', 'Lab 3 — Your Challenge'),
    ('labs.html', 'Keep Learning'),
]

def lesson_navigation(target):
    if target not in [url for url, _ in SEQUENCE]:
        return '', ''
    i = next(i for i, (url, _) in enumerate(SEQUENCE) if url == target)
    items = ''.join(f'<li><a href="{url}"' + (' aria-current="page"' if url == target else '') + f'>{html.escape(label)}</a></li>' for url, label in SEQUENCE)
    before = SEQUENCE[i-1] if i else ('workshop.html', 'Workshop overview')
    after = SEQUENCE[i+1] if i+1 < len(SEQUENCE) else ('workshop.html', 'Workshop overview')
    return f'<nav class="lesson-sequence" aria-label="Workshop sequence"><h2>Workshop</h2><ol>{items}</ol></nav>', f'<nav class="lesson-pagination" aria-label="Lesson navigation"><a href="{before[0]}">Previous: {html.escape(before[1])}</a><a href="{after[0]}">Next: {html.escape(after[1])}</a></nav>'

def shell(title, content, active=''):
    is_progression = active == 'full-progression.html'
    page_style = '<link rel="stylesheet" href="assets/progression.css">' if is_progression else ''
    page_class = ' class="full-progression"' if is_progression else ''
    if active in [url for url, _ in SEQUENCE[:-1]] or active == 'workbook.html':
        active = 'workshop.html'
    nav = [('index.html', 'Home'), ('workshop.html', 'Workshop'), ('labs.html', 'More labs'), ('progression.html', 'Learning map'), ('instructors.html', 'For instructors')]
    links = ''.join(f'<a href="{url}"' + (' aria-current="page"' if url == active else '') + f'>{label}</a>' for url, label in nav)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | AI Learning Lab</title><meta name="description" content="Student workshops and hands-on labs for learning to work with AI. Start at ASK and practice Define, Direct, Check, Adjust.">
<link rel="stylesheet" href="assets/site.css">{page_style}<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"></head>
<body{page_class}><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="index.html"><span class="mark" aria-hidden="true">AI</span>Learning Lab</a><nav aria-label="Main navigation">{links}</nav></header>
<main id="main">{content}</main><footer><strong>AI Learning Lab</strong><span>Start where you are. Move one step.</span><a href="https://github.com/luminerdy/AILearningLab">View on GitHub</a></footer></body></html>'''

def rewrite_links(body):
    for source, (target, _, _) in PAGES.items():
        body = body.replace(f'href="{source}"', f'href="{target}"')
    return body

def write_lesson(text, target, title, label, download_source):
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
    body = rewrite_links(md.convert(text))
    body = re.sub(r'<table>(.*?)</table>', r'<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table"><table>\1</table></div>', body, flags=re.S)
    download = f'<a class="text-link" href="downloads/{download_source}" download>Download editable Markdown</a>'
    sequence, pagination = lesson_navigation(target)
    content = f'<div class="page-intro"><p class="eyebrow">{label}</p>{download}</div><div class="reading-layout"><aside class="contents">{sequence}<h2>On this page</h2>{md.toc}</aside><article class="prose">{body}{pagination}</article></div>'
    if target == 'full-progression.html':
        content = progression_layout(body, download)
    (OUT / target).write_text(shell(title, content, target), encoding='utf-8')

def progression_layout(body, download):
    """Present the Markdown content in the reference artifact's card layout."""
    tree = ET.fromstring('<div>' + body + '</div>')
    hero = ET.Element('div', {'class': 'progression-hero'})
    eyebrow = ET.SubElement(hero, 'p', {'class': 'eyebrow'})
    eyebrow.text = 'HUMAN LEARNING PROGRESSION'
    sections = []
    current = hero
    for node in list(tree):
        if node.tag == 'h2':
            current = ET.Element('section', {'class': 'progression-section', 'aria-labelledby': node.get('id', '')})
            sections.append(current)
        current.append(node)
    nav = ET.Element('nav', {'class': 'section-nav', 'aria-label': 'Document sections'})
    for section in sections:
        heading = section.find('h2')
        link = ET.SubElement(nav, 'a', {'href': '#' + heading.get('id', '')})
        link.text = ''.join(heading.itertext())
    for section in sections:
        section_id = section.find('h2').get('id', '')
        if section_id == 'the-progression':
            lists = section.findall('ul')
            for i, listing in enumerate(lists):
                listing.set('class', 'practice-ladder' if i == 0 else 'self-location-map')
                for item in listing:
                    name = ''.join(item.itertext()).strip()
                    if name.startswith('ASK'):
                        item.set('class', 'ask-entry')
                    elif name.startswith(('ASSIST', 'SUGGEST')):
                        item.set('class', 'historical')
            # Preserve the Markdown wording while presenting self-location as a line.
            children = list(section)
            start = next(i for i, child in enumerate(children) if child.tag == 'h3' and child.get('id') == 'find-yourself-on-the-line')
            panel = ET.Element('div', {'class': 'self-map', 'aria-labelledby': 'find-yourself-on-the-line'})
            legend = ET.Element('div', {'class': 'map-key'})
            reflection = ET.Element('div', {'class': 'assessment-grid'})
            for child in children[start:]:
                section.remove(child)
                text = ''.join(child.itertext()).strip()
                if child.tag == 'ul':
                    child.set('class', 'map-line')
                    panel.append(child)
                elif child.tag == 'p' and text.startswith(('Comfortable:', 'Experimented:', '★')):
                    child.set('class', 'key-item')
                    marker = ET.Element('span', {'class': 'key-dot' if text.startswith('Comfortable:') else 'key-ring' if text.startswith('Experimented:') else 'key-star', 'aria-hidden': 'true'})
                    if text.startswith('★'):
                        marker.text = '★'
                        child.text = (child.text or '').replace('★', '').strip()
                    child.insert(0, marker)
                    legend.append(child)
                elif child.tag == 'p' and text.startswith(('Where am I', 'What have I', 'What would help')):
                    reflection.append(child)
                else:
                    panel.append(child)
            panel.append(legend)
            panel.append(reflection)
            section.append(panel)
        # Group each h3 and its following content as a card, without duplicating prose.
        if section_id in ('checking-grows-with-you', 'define-does-not-mean-write-the-complete-spec', 'this-is-familiar-agile-was-solving-the-same-uncertainty', 'what-actually-changes'):
            children = list(section)
            cards = ET.Element('div', {'class': 'concept-cards checks' if section_id == 'checking-grows-with-you' else 'concept-cards'})
            card = None
            for child in children:
                if child.tag == 'h3':
                    card = ET.SubElement(cards, 'div', {'class': 'concept-card'})
                if card is not None:
                    section.remove(child)
                    card.append(child)
            if len(cards):
                section.append(cards)
        if section_id == 'you-dont-have-to-start-at-the-beginning':
            children = list(section)
            route = ET.Element('div', {'class': 'entry-route'})
            for child in children[3:]:
                section.remove(child)
                route.append(child)
            section.append(route)
        if section_id == 'the-human-loop-never-goes-away':
            for child in list(section):
                if child.tag == 'p' and ''.join(child.itertext()).startswith('DEFINE →'):
                    index = list(section).index(child)
                    section.remove(child)
                    loop = ET.Element('div', {'class': 'human-loop', 'aria-label': 'Define, Direct, Check, Adjust, repeat'})
                    for name in ('DEFINE', 'DIRECT', 'CHECK', 'ADJUST'):
                        ET.SubElement(loop, 'span', {'class': 'loop-pill'}).text = name
                        ET.SubElement(loop, 'span', {'class': 'loop-arrow', 'aria-hidden': 'true'}).text = '↻' if name == 'ADJUST' else '→'
                    section.insert(index, loop)
    output = ET.Element('article', {'class': 'progression-article'})
    output.append(hero)
    output.append(nav)
    for section in sections:
        output.append(section)
    return '<div class="progression-download">' + download + '</div>' + ET.tostring(output, encoding='unicode', method='html')

for source, (target, title, label) in PAGES.items():
    write_lesson((CONTENT / source).read_text(encoding='utf-8'), target, title, label, source)

workbook = (CONTENT / 'workshop-student-workbook.md').read_text(encoding='utf-8')
def portion(start, end=None):
    return workbook.split(start, 1)[1].split(end, 1)[0] if end else workbook.split(start, 1)[1]
start = portion('## Your starting point', '## LLM basics warmup')
facts = portion('## Event facts', '## Your first lab')
first = portion('## Your first lab', '### Check the response')
checks = portion('### Check the response', '## Your independent challenge')
challenge = portion('## Your independent challenge')
write_lesson('# Lab 1 Ask\n\nDefine your goal and make your first request. Save the response; you will check and improve it in Lab 2. Checking matters from the beginning: read what comes back and note anything unexpected.\n\n## Your starting point\n'+start+'\n## Event facts\n'+facts+'\n## Create your announcement\n'+first, 'lab-1-ask.html', 'Lab 1 — Ask', 'WORKSHOP LAB 1', 'workshop-student-workbook.md')
write_lesson('# Lab 2 Check and Adjust\n\nContinue with your announcement from Lab 1. Use the event facts as evidence, then revise and recheck.\n\n## Event facts\n'+facts+'\n## Check the response\n'+checks, 'lab-2-check-adjust.html', 'Lab 2 — Check and Adjust', 'WORKSHOP LAB 2', 'workshop-student-workbook.md')
write_lesson('# Lab 3 Your Challenge\n\nComplete a new task using the full Define → Direct → Check → Adjust loop. Work individually and discuss ideas with classmates as you need.\n\n## Event facts\n'+facts+'\n## Choose your challenge\n'+challenge, 'lab-3-challenge.html', 'Lab 3 — Your Challenge', 'WORKSHOP LAB 3', 'workshop-student-workbook.md')

steps = ''.join(f'<a class="card" href="{url}"><span class="card-number">{i+1:02} / WORKSHOP</span><h2>{html.escape(label)}</h2><span class="card-link">Open lesson</span></a>' for i, (url, label) in enumerate(SEQUENCE))
overview = f'''<section class="map-intro"><p class="eyebrow">YOUR THREE-HOUR WORKSHOP</p><h1>Learn together.<br>Practice individually.</h1><p class="lead">Start with LLM Basics, then complete three labs. Keep your own prompts, results, checks, and revisions. Talk with classmates and ask for help as you work.</p><a class="button" href="llm-basics.html">Begin with LLM Basics</a></section><section class="route"><h2>Follow the workshop</h2><div class="cards">{steps}</div></section><section class="prose"><h2>Teaching or saving your work?</h2><p>Use the <a href="instructors.html">instructor guide</a> for timing, demonstrations, and teaching notes in this same sequence. The <a href="workbook.html">complete student workbook</a> brings all recording prompts together and includes a Markdown download.</p><p>After the workshop, choose a follow-on lab from Keep Learning. You can return to any lesson when it helps your work.</p></section>'''
(OUT / 'workshop.html').write_text(shell('Workshop', overview, 'workshop.html'), encoding='utf-8')

home = '''<section class="opening"><div><p class="eyebrow">A PRACTICE SPACE FOR WORKING WITH AI</p><h1>Ask. Try.<br>Check. Improve.</h1><p class="lead">Learn to turn an idea into a useful result—and show why it works. Start with everyday language. No coding experience needed.</p><div class="actions"><a class="button" href="workshop.html">Start the student workshop</a><a class="text-link" href="instructors.html">Teaching a group?</a></div><p class="meta">3-hour introduction · Individual labs and open discussion · More to explore afterward</p></div><div class="loop-panel"><p class="eyebrow">YOUR LEARNING LOOP</p><ol><li><span>01</span><div><strong>Define</strong><p>What do I want to accomplish?</p></div></li><li><span>02</span><div><strong>Direct</strong><p>What does AI need to know?</p></div></li><li><span>03</span><div><strong>Check</strong><p>What would convince me this is right?</p></div></li><li><span>04</span><div><strong>Adjust</strong><p>What should I change and try again?</p></div></li></ol><p class="loop-note">Repeat as you learn.</p></div></section>
<section class="route"><div class="section-heading"><p class="eyebrow">CHOOSE YOUR NEXT PRACTICE</p><h2>The workshop is your starting point.</h2><p>Make something small, test it against your goal, and build from there.</p></div><div class="cards"><a class="card" href="workshop.html"><span class="card-number">01 / START</span><h3>Learn to ASK</h3><p>Create a club announcement, check the facts, revise it, and document what changed; classmates can offer feedback.</p><span class="card-link">Open the workbook</span></a><a class="card" href="labs.html"><span class="card-number">02 / PRACTICE</span><h3>Keep experimenting</h3><p>Try five follow-on labs: adapt a message, create a study helper, write a project brief, capture a procedure, and build a small project.</p><span class="card-link">Explore the labs</span></a><a class="card" href="progression.html"><span class="card-number">03 / REFLECT</span><h3>Find your next step</h3><p>Notice what you can repeat confidently, what you have tried, and what would help your work next.</p><span class="card-link">View the learning map</span></a></div></section>
<section class="question"><p class="eyebrow">A HABIT FROM DAY ONE</p><h2>“What would convince me<br>this is right?”</h2><p>Check facts against the information you supplied. Test a result against your criteria. Ask another person to try it. An AI explanation can guide your checks; evidence gives you a reason to trust.</p></section>
<section class="instructor-strip"><div><h2>Bring the lab into your classroom.</h2><p>Use a three-hour workshop, split it across classes, or grow it into several days.</p></div><a class="button secondary" href="instructors.html">Open the instructor guide</a></section>'''
(OUT / 'index.html').write_text(shell('Learn to work with AI', home, 'index.html'), encoding='utf-8')

stages = [('ASK', 'I describe intent.'), ('COLLABORATE', 'I iterate with AI.'), ('ORIENT', 'I provide context and instructions.'), ('TEACH', 'I capture reusable know-how.'), ('ENABLE', 'I connect useful tools.'), ('DELEGATE', 'I give bounded goals.'), ('ORCHESTRATE', 'I design human + AI workflows.')]
stage_html = ''.join(f'<li><span class="card-number">{i:02}</span><h3>{name}</h3><p>{desc}</p></li>' for i, (name, desc) in enumerate(stages, 1))
progression = f'''<section class="map-intro"><p class="eyebrow">HUMAN LEARNING PROGRESSION</p><h1>Start where you are.<br>Move one step.</h1><p class="lead">This is a learning map, not a maturity score. Choose the practice that helps with the work in front of you.</p></section><ol class="stage-grid">{stage_html}</ol><section class="prose"><h2>Find yourself on the map</h2><p>For each practice, ask: Can I use this intentionally and repeatedly? Have I experimented with it? Would learning it help me next?</p><p>You can start directly at ASK. ASSIST and SUGGEST describe earlier developer tools; they are not prerequisites. You do not need to reach ORCHESTRATE.</p><h2>Strengthen how you check</h2><ol><li><strong>Black-box behavior:</strong> Does the result do what I wanted?</li><li><strong>Gray-box inspection:</strong> Can I inspect the important pieces?</li><li><strong>Evidence-based checking:</strong> Can I test against criteria and known results?</li><li><strong>Engineering checking:</strong> Is it fit for dependable use?</li></ol><p>The checks build on each other. Choose evidence that fits the task and strengthen it as consequences increase.</p><h2>Learn before you specify everything</h2><p>Define enough to take a useful next step. Explore, try, observe, and adjust. A more precise specification can be an output of learning.</p><a class="button secondary" href="full-progression.html">Read the full progression document</a></section>'''
(OUT / 'progression.html').write_text(shell('Learning map', progression, 'progression.html'), encoding='utf-8')
(OUT / 'downloads').mkdir(exist_ok=True)
for source in PAGES:
    shutil.copy2(CONTENT / source, OUT / 'downloads' / source)
shutil.copytree(ROOT / 'site' / 'assets', OUT / 'assets', dirs_exist_ok=True)
(OUT / '.nojekyll').touch()
(OUT / '404.html').write_text(shell('Page not found', '<section class="map-intro"><p class="eyebrow">PAGE NOT FOUND</p><h1>Find your next practice.</h1><p>This page may have moved as the lab develops.</p><a class="button" href="/AILearningLab/">Return to AI Learning Lab</a></section>'), encoding='utf-8')
print(f'Built {len(list(OUT.glob("*.html")))} HTML pages in {OUT}')


