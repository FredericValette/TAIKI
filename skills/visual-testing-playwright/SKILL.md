---
name: visual-testing-playwright
description: Validate rendered interfaces with reproducible Playwright screenshots and documented visual differences.
---

# Visual Testing with Playwright

Capture and compare user-interface states in a repeatable browser environment.

## Workflow

1. Confirm target URL, browser, viewport, test data, and baseline revision.
2. Exercise the requested page states using stable selectors and explicit waits.
3. Capture screenshots and browser errors; distinguish layout changes from rendering noise.
4. Report reproducible differences, affected viewport, and supporting artifacts.

Do not approve visual changes solely from a single viewport or suppress diffs without a documented reason. Use the prompt and output contract in this directory.