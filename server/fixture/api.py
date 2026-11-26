import os
from typing import Annotated
from uuid import UUID

from fastapi import Depends, FastAPI, Header, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, SQLAlchemyError, TimeoutError

from fixture.database import engine_for, schema_ready

engine = engine_for("api")
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("RAFIQ_WEB_ORIGIN", "http://127.0.0.1:3000")],
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization"],
)

IDENTITIES = {"Bearer local-driver-a": "driver-a", "Bearer local-driver-b": "driver-b"}


@app.middleware("http")
async def prevent_fixture_caching(request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    return response


def fixture_owner(authorization: Annotated[str | None, Header()] = None) -> str:
    owner = IDENTITIES.get(authorization)
    if owner is None:
        raise HTTPException(401, "Synthetic identity required", {"WWW-Authenticate": "Bearer"})
    return owner


Owner = Annotated[str, Depends(fixture_owner)]


@app.exception_handler(OperationalError)
@app.exception_handler(TimeoutError)
async def database_unavailable(_request, _error):
    return JSONResponse(status_code=503, content={"detail": "Fixture database unavailable"})


def use_owner(connection, owner: str):
    try:
        compatible = schema_ready(connection, "api")
    except SQLAlchemyError:
        compatible = False
    if not compatible:
        raise HTTPException(503, "Fixture database unavailable")
    connection.execute(
        text("SELECT set_config('rafiq.fixture_owner', :owner, true)"), {"owner": owner}
    )


@app.get("/internal/livez")
def live():
    return {"status": "live"}


@app.get("/internal/readyz")
def ready(response: Response):
    try:
        with engine.connect() as connection:
            if schema_ready(connection, "api"):
                return {"status": "ready"}
    except SQLAlchemyError:
        pass
    response.status_code = 503
    return {"status": "unavailable"}


@app.post("/api/v1/local-fixtures")
def submit(owner: Owner):
    with engine.begin() as connection:
        use_owner(connection, owner)
        connection.execute(
            text("""
                INSERT INTO rafiq_fixture.fixtures (owner_id)
                VALUES (:owner) ON CONFLICT (owner_id) DO NOTHING
            """),
            {"owner": owner},
        )
        row = connection.execute(
            text("SELECT id, status, result FROM rafiq_fixture.fixtures WHERE owner_id = :owner"),
            {"owner": owner},
        ).mappings().one()
    return dict(row)


@app.get("/api/v1/local-fixtures/current")
def current(owner: Owner):
    with engine.begin() as connection:
        use_owner(connection, owner)
        row = connection.execute(
            text("SELECT id, status, result FROM rafiq_fixture.fixtures WHERE owner_id = :owner"),
            {"owner": owner},
        ).mappings().one_or_none()
    return dict(row) if row is not None else None


@app.get("/api/v1/local-fixtures/{fixture_id}")
def get_fixture(fixture_id: UUID, owner: Owner):
    with engine.begin() as connection:
        use_owner(connection, owner)
        row = connection.execute(
            text("SELECT id, status, result FROM rafiq_fixture.fixtures WHERE id = :id"),
            {"id": fixture_id},
        ).mappings().one_or_none()
    if row is None:
        raise HTTPException(404, "Fixture not found")
    return dict(row)
