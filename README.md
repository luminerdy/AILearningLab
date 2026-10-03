# AI Learning Lab

Learn to work with AI through practice, evidence, and reflection.

**Students and instructors: use the [AI Learning Lab website](https://luminerdy.github.io/AILearningLab/).** All training materials and editable downloads are available there.

- [Start the workshop](https://luminerdy.github.io/AILearningLab/workshop.html)
- [LLM basics](https://luminerdy.github.io/AILearningLab/llm-basics.html)
- [Instructor guide](https://luminerdy.github.io/AILearningLab/instructors.html)
- [Student workbook](https://luminerdy.github.io/AILearningLab/workbook.html)
- [Keep learning](https://luminerdy.github.io/AILearningLab/labs.html)
- [Human learning progression](https://luminerdy.github.io/AILearningLab/full-progression.html)

## Maintain the website

This repository holds the website's build sources. Edit curriculum in `site/content/`, styling in `site/assets/`, and page generation in `scripts/build_site.py`.

To preview a build:

```sh
python -m pip install -r requirements-site.txt
python scripts/build_site.py
python -m http.server --directory docs 8000
```

Pushing to `main` builds and deploys GitHub Pages through GitHub Actions. Generated `docs/` files are not committed; the website is the reading destination for the training materials.
