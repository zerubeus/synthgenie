FROM python:3.12-slim

WORKDIR /app

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
COPY README.md ./
COPY synthgenie ./synthgenie

RUN pip install --no-cache-dir .

EXPOSE 8000

# Add health check directly to Dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/docs || exit 1

# Use environment variable for port if provided
ENV PORT=8000
CMD uvicorn synthgenie.app:app --host 0.0.0.0 --port ${PORT} 