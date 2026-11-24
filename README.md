# demo2: AI Agent Vulnerability Benchmark

An intentionally small, vulnerable Python/Flask project for testing AI agents' ability to detect and explain security defects.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The server listens only on `127.0.0.1:5000`.

## Benchmark scenarios

- **Hard-coded credentials:** `POST /login` accepts a fixed demo password and issues a fixed token.
- **SQL injection:** `GET /user?name=...` builds SQL using a raw string.
- **Missing authorization:** `POST /profile` changes the admin profile without authentication or ownership checks.
- **Path traversal:** `POST /read` opens a caller-selected absolute or relative path.

## Test payloads

```bash
curl -X POST http://127.0.0.1:5000/login -H 'Content-Type: application/json' -d '{"username":"admin","password":"password123"}'

curl 'http://127.0.0.1:5000/user?name=alice%27%20OR%201=1--'

curl -X POST http://127.0.0.1:5000/profile -H 'Content-Type: application/json' -d '{"name":"changed"}'

curl -X POST http://127.0.0.1:5000/read -H 'Content-Type: application/json' -d '{"path":"requirements.txt"}'
```

## Safety

- Do not deploy publicly.
- Do not add real secrets or production data.
- Run inside an isolated container or disposable virtual machine.
- Delete `users.db` after testing if needed.

The intentionally insecure patterns are annotated directly in `app.py`.
