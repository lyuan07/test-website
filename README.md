# Test Website

Disposable static website for Agent Taro ticket-to-code testing. It was copied from the Agent X website fixture into a separate repository so the interview project remains unchanged.

Live site: [lyuan07.github.io/test-website](https://lyuan07.github.io/test-website/)

## Run locally

```bash
python3 -m http.server 8000 --directory site
```

Open <http://localhost:8000>.

## Test

```bash
python3 -m unittest discover -s tests -v
```

Keep changes synthetic. Do not add credentials, customer data, private screenshots, or production integrations.

## Deployment

GitHub Pages publishes the root of the `gh-pages` branch. Agent Taro changes `main`; after an approved change is merged and independently verified, update `gh-pages` from the contents of `site/`. Deployment remains a separate human-approved step.
