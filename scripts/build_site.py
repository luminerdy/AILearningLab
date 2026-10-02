"""Build the public learning site from the workshop Markdown sources."""
from pathlib import Path
import html
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.site-tools'))
import markdown

OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
PAGES = {
    'workshop-student-workbook.md': ('workshop.html', 'Student workshop', 'START AT ASK'),
    'learning-path.md': ('labs.html', 'Keep learning', 'AFTER THE WORKSHOP'),
    'workshop-facilitator-guide.md': ('instructors.html', 'Instructor guide', 'TEACH THE WORKSHOP'),
}

def shell(title, content, active=''):
    nav = [('index.html', 'Home'), ('workshop.html', 'Workshop'), ('labs.html', 'More labs'), ('progression.html', 'Learning map'), ('instructors.html', 'For instructors')]
    links = ''.join(f'<a href="{url}"' + (' aria-current="page"' if url == active else '') + f'>{label}</a>' for url, label in nav)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | AI Learning Lab</title><meta name="description" content="Student workshops and hands-on labs for learning to work with AI. Start at ASK and practice Define, Direct, Check, Adjust.">
<link rel="stylesheet" href="assets/site.css"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"></head>
<body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="index.html"><span class="mark" aria-hidden="true">AI</span>Learning Lab</a><nav aria-label="Main navigation">{links}</nav></header>
<main id="main">{content}</main><footer><strong>AI Learning Lab</strong><span>Start where you are. Move one step.</span><a href="https://github.com/luminerdy/AILearningLab">View on GitHub</a></footer></body></html>'''

def rewrite_links(body):
    body = body.replace('href="agentic-ai-learning-progression-updated.html"', 'href="full-progression.html"')
    for source, (target, _, _) in PAGES.items():
        body = body.replace(f'href="{source}"', f'href="{target}"')
    return body

for source, (target, title, label) in PAGES.items():
    text = (ROOT / source).read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
    body = rewrite_links(md.convert(text))
    body = re.sub(r'<table>(.*?)</table>', r'<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table"><table>\1</table></div>', body, flags=re.S)
    download = f'<a class="text-link" href="downloads/{source}" download>Download editable Markdown</a>'
    content = f'<div class="page-intro"><p class="eyebrow">{label}</p>{download}</div><div class="reading-layout"><aside class="contents"><h2>On this page</h2>{md.toc}</aside><article class="prose">{body}</article></div>'
    (OUT / target).write_text(shell(title, content, target), encoding='utf-8')

home = '''<section class="opening"><div><p class="eyebrow">A PRACTICE SPACE FOR WORKING WITH AI</p><h1>Ask. Try.<br>Check. Improve.</h1><p class="lead">Learn to turn an idea into a useful result—and show why it works. Start with everyday language. No coding experience needed.</p><div class="actions"><a class="button" href="workshop.html">Start the student workshop</a><a class="text-link" href="instructors.html">Teaching a group?</a></div><p class="meta">3-hour introduction · Paired practice · More to explore afterward</p></div><div class="loop-panel"><p class="eyebrow">YOUR LEARNING LOOP</p><ol><li><span>01</span><div><strong>Define</strong><p>What do I want to accomplish?</p></div></li><li><span>02</span><div><strong>Direct</strong><p>What does AI need to know?</p></div></li><li><span>03</span><div><strong>Check</strong><p>What would convince me this is right?</p></div></li><li><span>04</span><div><strong>Adjust</strong><p>What should I change and try again?</p></div></li></ol><p class="loop-note">Repeat as you learn.</p></div></section>
<section class="route"><div class="section-heading"><p class="eyebrow">CHOOSE YOUR NEXT PRACTICE</p><h2>The workshop is your starting point.</h2><p>Make something small, test it against your goal, and build from there.</p></div><div class="cards"><a class="card" href="workshop.html"><span class="card-number">01 / START</span><h3>Learn to ASK</h3><p>Create a club announcement, check the facts, revise it, and compare the results with a partner.</p><span class="card-link">Open the workbook</span></a><a class="card" href="labs.html"><span class="card-number">02 / PRACTICE</span><h3>Keep experimenting</h3><p>Try five follow-on labs: adapt a message, create a study helper, write a project brief, capture a procedure, and build a small project.</p><span class="card-link">Explore the labs</span></a><a class="card" href="progression.html"><span class="card-number">03 / REFLECT</span><h3>Find your next step</h3><p>Notice what you can repeat confidently, what you have tried, and what would help your work next.</p><span class="card-link">View the learning map</span></a></div></section>
<section class="question"><p class="eyebrow">A HABIT FROM DAY ONE</p><h2>“What would convince me<br>this is right?”</h2><p>Check facts against the information you supplied. Test a result against your criteria. Ask another person to try it. An AI explanation can guide your checks; evidence gives you a reason to trust.</p></section>
<section class="instructor-strip"><div><h2>Bring the lab into your classroom.</h2><p>Use a three-hour workshop, split it across classes, or grow it into several days.</p></div><a class="button secondary" href="instructors.html">Open the instructor guide</a></section>'''
(OUT / 'index.html').write_text(shell('Learn to work with AI', home, 'index.html'), encoding='utf-8')

stages = [('ASK', 'I describe intent.'), ('COLLABORATE', 'I iterate with AI.'), ('ORIENT', 'I provide context and instructions.'), ('TEACH', 'I capture reusable know-how.'), ('ENABLE', 'I connect useful tools.'), ('DELEGATE', 'I give bounded goals.'), ('ORCHESTRATE', 'I design human + AI workflows.')]
stage_html = ''.join(f'<li><span class="card-number">{i:02}</span><h3>{name}</h3><p>{desc}</p></li>' for i, (name, desc) in enumerate(stages, 1))
progression = f'''<section class="map-intro"><p class="eyebrow">HUMAN LEARNING PROGRESSION</p><h1>Start where you are.<br>Move one step.</h1><p class="lead">This is a learning map, not a maturity score. Choose the practice that helps with the work in front of you.</p></section><ol class="stage-grid">{stage_html}</ol><section class="prose"><h2>Find yourself on the map</h2><p>For each practice, ask: Can I use this intentionally and repeatedly? Have I experimented with it? Would learning it help me next?</p><p>You can start directly at ASK. ASSIST and SUGGEST describe earlier developer tools; they are not prerequisites. You do not need to reach ORCHESTRATE.</p><h2>Strengthen how you check</h2><ol><li><strong>Black-box behavior:</strong> Does the result do what I wanted?</li><li><strong>Gray-box inspection:</strong> Can I inspect the important pieces?</li><li><strong>Evidence-based checking:</strong> Can I test against criteria and known results?</li><li><strong>Engineering checking:</strong> Is it fit for dependable use?</li></ol><p>The checks build on each other. Choose evidence that fits the task and strengthen it as consequences increase.</p><h2>Learn before you specify everything</h2><p>Define enough to take a useful next step. Explore, try, observe, and adjust. A more precise specification can be an output of learning.</p><a class="button secondary" href="full-progression.html">Read the full progression document</a></section>'''
(OUT / 'progression.html').write_text(shell('Learning map', progression, 'progression.html'), encoding='utf-8')
shutil.copy2(ROOT / 'agentic-ai-learning-progression-updated.html', OUT / 'full-progression.html')
(OUT / 'downloads').mkdir(exist_ok=True)
for source in PAGES:
    shutil.copy2(ROOT / source, OUT / 'downloads' / source)
shutil.copytree(ROOT / 'site' / 'assets', OUT / 'assets', dirs_exist_ok=True)
(OUT / '.nojekyll').touch()
(OUT / '404.html').write_text(shell('Page not found', '<section class="map-intro"><p class="eyebrow">PAGE NOT FOUND</p><h1>Find your next practice.</h1><p>This page may have moved as the lab develops.</p><a class="button" href="/AILearningLab/">Return to AI Learning Lab</a></section>'), encoding='utf-8')
print(f'Built {len(list(OUT.glob("*.html")))} HTML pages in {OUT}')
