# Plan

The latest operator review requests "make the website green", superseding the original pink request. This run has no ratified spec or explicit acceptance criteria.

1. Update the six existing theme tokens in `site/styles.css` to a coordinated green palette. These tokens control the brand accents, tinted surfaces, borders, and page background. Preserve the existing HTML, layout, responsive rules, and dependency-free setup.
2. Update the palette regression test in `tests/test_site.py` to assert the green theme values and rename it to describe the current requirement.
3. Run `python3 -m unittest discover -s tests -v`, run `git diff --check`, and review the final diff. The repository is a static website with no build step. Leave deployment and merging for human review.

## Baseline

- Working tree was clean before changes.
- All 4 existing tests passed.
- Baseline failing tests: none.
