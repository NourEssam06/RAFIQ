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
RUN mkdir -p /opt/rafiq-r \
    && (curl -fsSL https://cran.r-project.org/src/contrib/renv_1.3.1.tar.gz -o /tmp/rafiq-renv.tar.gz \
      || curl -fsSL https://cran.r-project.org/src/contrib/Archive/renv/renv_1.3.1.tar.gz -o /tmp/rafiq-renv.tar.gz) \
    && echo 'e16281908ddf0ed6f8f6f8ad3f2cc4788af6de04c1ab223517aa1cc9acb30731  /tmp/rafiq-renv.tar.gz' | sha256sum -c - \
    && R CMD INSTALL --library=/opt/rafiq-r /tmp/rafiq-renv.tar.gz \
    && Rscript --vanilla -e 'renv::restore(project="/app", library="/opt/rafiq-r", prompt=FALSE)' \
    && rm /tmp/rafiq-renv.tar.gz
COPY fixture ./fixture
COPY r ./r
COPY tests ./tests
USER 10001:10001
CMD ["python", "-m", "fixture.worker"]
