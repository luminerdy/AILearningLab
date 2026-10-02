# AI Learning Lab

Learn to work with AI through practice, evidence, and reflection. Start at **ASK** using everyday language. Use **Define → Direct → Check → Adjust** to improve a result and explain why it meets your goal.

The learning website is designed for GitHub Pages at `https://luminerdy.github.io/AILearningLab/`.

This repository is being developed for student workshops and continued independent learning, with material adaptable for older audiences. The live introduction is three hours. The learning path extends beyond it and can support several days of instruction.

## Start the workshop

- Instructors: use the [facilitator guide](workshop-facilitator-guide.md) for preparation, the three-hour agenda, demonstration, exercises, and assessment.
- Students: work through the [student workbook](workshop-student-workbook.md), saving your requests, results, checks, and revisions.
- After the workshop: choose a lab from the [continued learning path](learning-path.md).

No coding experience is required for the introductory workshop. Student-provided ChatGPT Plus accounts are under consideration; the access requirement has not been finalized. The introductory tasks use text requests and supplied facts.

## Keep learning

The progression is **ASK → COLLABORATE → ORIENT → TEACH → ENABLE → DELEGATE → ORCHESTRATE**. Choose practices that help your task. You do not need to reach the end of the line. Historical ASSIST and SUGGEST stages are not prerequisites.

For each exercise, save a goal, request, result, checks, revision, and reflection. Use fictional or non-sensitive examples when sharing work. You can read the materials on GitHub without creating a repository of your own; keep work locally or in the class system unless your instructor asks you to publish it.

## Founding documents

- [Human learning progression](agentic-ai-learning-progression-updated.html) explains the framework, checking progression, and self-location map. Download and open the HTML in a browser to view its designed layout.

The conversation transcript and workspace memory are retained locally for continuity.

The workshop activities are new curriculum drafts based on those documents. Delivery results will guide future revisions.

## Update the website

Edit the workshop Markdown files or `learning-path.md` to update the learning content. Edit `scripts/build_site.py` for the home page and learning map; edit `site/assets/site.css` for the shared design.

Install the build dependency with `python -m pip install -r requirements-site.txt`, then run `python scripts/build_site.py`. Preview with `python -m http.server 8765 --directory docs` and open `http://localhost:8765`.

Changes pushed to `main` trigger `.github/workflows/pages.yml`, which rebuilds and publishes the website. In repository Settings → Pages, select **GitHub Actions** as the source. See [GitHub Pages publishing guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
