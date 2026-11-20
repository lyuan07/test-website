# Test Website

Disposable static website for Agent Taro ticket-to-code testing. It was copied from the Agent X website fixture into a separate repository so the interview project remains unchanged.

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
