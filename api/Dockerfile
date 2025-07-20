FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Runtime tuning, unbuffered logs, and writable cache path
ENV UV_COMPILE_BYTECODE=1 \
  UV_LINK_MODE=copy \
  UV_HTTP_TIMEOUT=600 \
  UV_NO_INTERACTION=1 \
  PYTHONUNBUFFERED=1 \
  XDG_CACHE_HOME=/home/app/.cache

WORKDIR /code

# Non-root user with a real home directory
RUN adduser --system --uid 1001 --home /home/app app \
  && mkdir -p /home/app/.cache

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/home/app/.cache/uv \
  uv sync --locked --no-install-project --no-editable

# Application source and project install
COPY . .
RUN --mount=type=cache,target=/home/app/.cache/uv \
  uv sync --locked --no-editable

# Activate the virtual environment created by uv sync
ENV PATH="/code/.venv/bin:$PATH"

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/docs || exit 1

CMD ["uvicorn", "synthgenie.app:app", "--host", "0.0.0.0", "--port", "8000"]