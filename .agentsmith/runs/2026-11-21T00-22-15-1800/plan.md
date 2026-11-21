# Implementation plan

Request: make the website pink. No acceptance criteria or ratified spec were supplied.

Baseline: `python3 -m unittest discover -s tests -v` passed all 3 tests; the working tree was clean.

1. Update the existing theme tokens in `site/styles.css` to use deep pink accents, pale pink highlights and canvas, and pink borders. Preserve semantic HTML, layout, responsive rules, and dependencies.
2. Add a regression test in `tests/test_site.py` for the pink palette while retaining the existing theme and page structure checks.
3. Run `python3 -m unittest discover -s tests -v` and review the diff with `git diff --check` and `git diff -- site/styles.css tests/test_site.py`.

This static website has no separate build step. Do not merge or deploy.
