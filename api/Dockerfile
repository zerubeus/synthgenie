FROM python:3.13-alpine@sha256:18159b2be11db91f84b8f8f655cd860f805dbd9e49a583ddaac8ab39bf4fe1a7

WORKDIR /app

# Install curl for health checks
RUN apk add --no-cache curl

COPY pyproject.toml ./
COPY README.md ./

RUN pip install --no-cache-dir .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/docs || exit 1

ENV PORT=8000

CMD ["sh", "-c", "uvicorn synthgenie.app:app --host 0.0.0.0 --port ${PORT} --reload"] 