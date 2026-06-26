# Development setup

## Runtime versions

- Python 3.11+
- Node.js 22.13+ or 24+


## Backend

```bash
cd backend
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
cp .env.example .env
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Useful endpoints:

- `GET /api/health/` - API health check
- `GET /api/schema/` - OpenAPI schema
- `GET /api/docs/` - Swagger UI

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The Vite dev server proxies `/api` requests to `http://127.0.0.1:8000`.

## Optional services

PostgreSQL with pgvector and Redis are available through Docker Compose:

```bash
docker compose up -d postgres redis
```

The scaffold defaults to SQLite and local-memory cache so it can run before PostgreSQL and Redis are configured.
