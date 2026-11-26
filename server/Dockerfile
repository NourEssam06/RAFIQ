FROM ghcr.io/astral-sh/uv:0.13.9@sha256:d3b601f0c7b118bc1753febf7c41cc80981df678445e0254284eecf84db79a7d AS uv

FROM python:3.14.10-slim-bookworm@sha256:e60ad028afdcdd14772a3d46decf0eaf616720f9102aeb4397a2045ff6718c3d AS api
COPY --from=uv /uv /usr/local/bin/uv
WORKDIR /app
ENV PATH="/app/.venv/bin:${PATH}" UV_PYTHON_DOWNLOADS=never PYTHONDONTWRITEBYTECODE=1
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev
COPY alembic.ini ./
COPY migrations ./migrations
COPY fixture ./fixture
USER 10001:10001
CMD ["uvicorn", "fixture.api:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]

FROM rocker/r-ver:4.6.2@sha256:b344cf44c8cfb787d9e091cb88a9694fbc771e7600edaa7b545030babfc05bf3 AS worker
COPY --from=uv /uv /usr/local/bin/uv
WORKDIR /app
ENV PATH="/app/.venv/bin:${PATH}" UV_PYTHON_INSTALL_DIR=/opt/uv-python \
    UV_PYTHON_PREFERENCE=only-managed PYTHONDONTWRITEBYTECODE=1 \
    R_LIBS_SITE=/opt/rafiq-r RENV_CONFIG_CACHE_ENABLED=false
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev
COPY renv.lock ./
COPY r/restore.R ./r/restore.R
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /opt/rafiq-r \
    && Rscript --vanilla r/restore.R
COPY fixture ./fixture
COPY r ./r
COPY tests ./tests
USER 10001:10001
CMD ["python", "-m", "fixture.worker"]
