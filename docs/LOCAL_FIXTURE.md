# Run the local browser-to-R fixture

Issue #5 implements FND-02 for modules M01, M03, M06 and M10 and prepares NFR-03 and NFR-05 evidence. This synthetic page has no product screen ID. Its only inputs are the two local identities and the built-in samples 2, 4 and 6. The expected result is three samples with a mean of 4 and method `synthetic-mean-v1`. [Issue #5](https://github.com/alisameh05/RAFIQ/issues/5) · [Implementation guide](IMPLEMENTATION_GUIDE.md#phase-0--running-foundation-and-qualification-intake)

## Clean startup

Use a working Docker Engine with Compose v2 or newer and Linux containers. On Windows, start Docker Desktop with its WSL 2 backend. From a clean checkout, run these commands. The example file already contains the synthetic settings.

```powershell
docker compose --env-file .env.fixture.example config --quiet
docker compose --env-file .env.fixture.example up --build --wait --wait-timeout 180
docker compose --env-file .env.fixture.example ps -a
```

The first build restores `web/package-lock.json` with npm, `server/uv.lock` with uv, and `server/renv.lock` with renv. Pin and restore the dependencies used by this slice according to the [TRD baseline](TRD.md#11-runtime-and-dependency-baseline). The Dockerfiles and Compose file pin upstream image index digests. The worker's uv version pins the managed Python download, and its Dockerfile verifies the renv bootstrap archive. The fixture workflow records observed runtime versions, image IDs and lockfile hashes.

| Service | Entry point and evidence |
| --- | --- |
| PostgreSQL | Private Compose network. The TCP health check waits for the official entry point to finish bootstrap. |
| Alembic | `migrate` runs `alembic upgrade head` once for startup under the migration login. API and worker wait for its successful exit. |
| Web | Open `http://127.0.0.1:3000`. `GET /healthz` confirms the Next.js process responds. |
| API | `GET /internal/livez` checks the process. `GET /internal/readyz` returns 200 when the expected schema revision is available under the API login, or 503 when unavailable. Use `http://127.0.0.1:8000`. |
| Worker | `python -m fixture.worker` checks the pinned R and jsonlite versions and processes PostgreSQL leases. `python -m fixture.worker --check-health` checks for a fresh heartbeat from the claim loop. |

The browser calls FastAPI directly. Use the literal loopback address above so the browser origin matches the CORS policy. The API resolves the bearer token to a fixed synthetic identity before opening an owner-scoped transaction. Choose Driver A, submit the fixture, wait for the result and reload. The same fixture UUID and result should appear. Driver B on an empty fixture volume starts with an empty history. The fixture API returns 401 without a recognized synthetic bearer and 404 for another driver's fixture UUID.

## PostgreSQL parity and role scope

The fixture uses the official PostgreSQL 17.12 Debian Bookworm image. PostgreSQL 17 is the local major-version target for the Supabase PostgreSQL 17 family. This slice uses core UUID, JSONB, transaction, row-locking and RLS features and requires zero extensions. Hosted project patch, extension inventory, TLS, pooler semantics and release readiness require evidence from the isolated hosted environment. [PostgreSQL 17.12 release](https://www.postgresql.org/docs/17/release-17-12.html) · [Supabase upgrade guidance](https://supabase.com/docs/guides/platform/upgrading)

The first startup creates the dedicated private fixture schema and three separate logins. Alembic owns DDL under the migration login. The API's transaction-local identity limits its RLS reads and inserts to the owner and its grants exclude updates. The worker can read only its job columns, claim queued or expired jobs, and update the lease and result columns. A publish succeeds only for the running job's current, unexpired generation. The fixture input and its one logical job share a row to commit both atomically. The result is available to the owner after the worker commits it.

The named `pgdata` volume is mounted at `/var/lib/postgresql/data`. A normal `docker compose --env-file .env.fixture.example down` preserves it. Use a unique Compose project and its fresh volume for a disposable cold run. For that disposable project only, `down --volumes` removes its database. Run one stack at a time because the browser and API use fixed loopback ports.

## Verification

The [local fixture workflow](https://github.com/alisameh05/RAFIQ/actions/workflows/local-fixture.yml) runs the clean build, real Chromium browser smoke, PostgreSQL role checks, R result and lease fencing checks, and a restart using the same volume. Reproduce the browser smoke on a fresh running stack with the pinned Node and npm versions.

```powershell
Push-Location web
npm ci
npm run typecheck
npm exec playwright install chromium
npm run test:e2e
Pop-Location
```

Optionally set `RAFIQ_BROWSER_CHANNEL=chrome` in your shell before the test to use installed Chrome. Once the browser smoke succeeds, stop the ordinary worker before running the deterministic role and lease tests. These tests submit Driver B's fixture, so use a fresh disposable volume for each full suite.

```powershell
docker compose --env-file .env.fixture.example stop worker
docker compose --env-file .env.fixture.example run --rm --no-deps -e RAFIQ_API_DATABASE_URL=postgresql+psycopg://rafiq_api:local-api-only@db:5432/rafiq worker python -m unittest discover -s tests -v
```

The fixture uses no provider credentials. Its public synthetic defaults require the explicit `local-fixture` mode and a disposable database. Real secrets and local logs belong in ignored files. Check with `git check-ignore .env server/.env.local web/debug.log logs/fixture.txt`. The committed `.env.fixture.example` contains public test values.
