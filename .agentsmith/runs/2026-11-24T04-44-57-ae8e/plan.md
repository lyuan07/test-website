# Ticket 9 implementation plan

Baseline: all four existing tests passed before edits.

1. Copy the approved PNG unchanged from `.agentsmith/reference/images/25130980353b462ba504133e96ce7ade.png` into `site/images/header.png`.
2. Replace the hero's product-card illustration in `site/index.html` with the local image. Preserve the hero text and navigation. Specify the intrinsic 853 × 638 dimensions and use an empty alt attribute because the image supplements the existing marketing copy.
3. Replace the illustration-specific rules in `site/styles.css` with responsive image styling that preserves the attachment's aspect ratio.
4. Extend `tests/test_site.py` to verify the hero image, committed asset integrity, intrinsic dimensions, and responsive styling. Run the full unittest suite and review the diff.

Requirement served: change the header image to the supplied attachment. No additional acceptance criteria were specified.
