# Repository guide

## Build, lint, and test

Run frontend commands from `frontend/`:

```sh
npm run dev
npm run build
npm run lint
```

There is currently no frontend test script or test framework. The backend uses Django's test runner; with the Compose stack running, run the API tests from the repository root:

```sh
docker compose exec backend python manage.py test api
docker compose exec backend python manage.py test api.tests.TestCaseName.test_method
```

`backend/api/tests.py` is currently only a placeholder. No separate backend lint command is configured.

## Architecture

- `frontend/` is a React application built with Vite. `src/main.jsx` mounts `App.jsx`; the current UI is still the Vite starter screen, and the frontend has not yet been connected to the API.
- `backend/` is a Django project. `config/urls.py` mounts the app's `api/urls.py` under `/api/` and exposes Django admin at `/admin/`. The implemented API endpoint is currently `GET /api/health/`; product, account, cart, and order features are planned rather than implemented.
- `compose.yaml` runs MariaDB, Django, and a production-built React site served by Nginx. Django reads database and runtime settings from environment variables; its container entrypoint runs Django migrations before starting the development server.
- `docs/database/la_pitayera.sql` creates the initial MariaDB schema, and `docs/diagramaER.md` describes its intended entities and relationships. Compose imports the SQL only when MariaDB initializes a fresh data volume. Keep schema changes aligned with these docs and any Django ORM models/migrations added later.

## Repository conventions

- Add API routes in `backend/api/urls.py`; `config/urls.py` supplies the `/api/` prefix. Keep backend settings configurable through the existing environment variables and use `.env.example` as the template for local configuration. Do not commit `.env`.
- The current frontend dependencies are React and React DOM only; do not assume the planned React Router or other README-listed features are already installed.
- Follow `docs/guia-estilo.md` for UI work: it defines the Pitaya/Hoja/Crema palette, 4 px spacing base, component styling, accessibility expectations, and responsive widths (360, 768, and 1280 px).
- The project README and design documentation are in Spanish; update the relevant documentation alongside changes to their documented behavior.
