# Ticket 9 operator-requested restoration

The operator requests restoration to the code state immediately before attempt 1, superseding the original image-change request.

## Established boundary

- Attempt 1: `1597e4929d5e9c0992baadc08b88efa3930af8cc`, identified by additions under `.agentsmith/runs/2026-11-24T04-44-57-ae8e/`.
- Pre-attempt state: `383e47af3da84ce5f43ccae732646b5ba4783dd9`.
- Commit messages contain no Run-Id trailers. The run-directory additions establish the boundary.
- The current `site/` and `tests/` contents match the attempt commit; there are no intervening source changes to reconcile.
- Baseline: all six tests pass with `python3 -m unittest discover -s tests -v`.

## Changes and verification

1. Reverse the attempt's patch only for `site/index.html`, `site/styles.css`, `tests/test_site.py`, and `site/images/header.png`. This restores the original product-card header, its responsive styling, and the pre-attempt tests, and removes the added image asset.
2. Preserve historical `.agentsmith/` records and framework metadata. Preserve the unrelated green theme and all other base-branch changes. Leave publication branches untouched.
3. Run the restored complete test suite, check whitespace, review the inverse diff, and assert that the complete tracked `site/` and `tests/` trees match the pre-attempt commit. Assert that all previously tracked framework metadata remains unchanged.
4. Record the restoration in a new inverse commit with a Run-Id trailer. Do not reset, rewrite shared history, merge, or deploy.

This dependency-free static site has no separate build step.
