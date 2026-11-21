# Plan: make the website pink

The ticket has no explicit acceptance criteria. Apply a visibly pink theme while preserving the existing content, semantic HTML, responsive layout, and dependency-free setup.

1. Update `site/styles.css`: replace the four existing indigo brand tokens with deep pink, dark pink, pale pink, and pink ink; give the canvas and borders pale pink tones. Existing components inherit these tokens.
2. Update `tests/test_site.py`: add regression coverage for the pink theme tokens while retaining the existing identity, structure, and theme-completeness checks.
3. Run `python3 -m unittest discover -s tests -v` and review the final diff with `git diff --check` and `git diff`.

Baseline: all 3 existing tests passed before changes; no baseline failures. This static website has no build step. No deployment or merge is part of this work.
