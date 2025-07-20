.PHONY: help install start start-prod lint format typecheck docker-up docker-down docker-logs db-shell clean

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make start        - Start development server"
	@echo "  make start-prod   - Start production server"
	@echo "  make lint         - Run linting checks"
	@echo "  make format       - Format code and fix linting issues"
	@echo "  make typecheck    - Run type checking with pyright"
	@echo "  make docker-up    - Start Docker services"
	@echo "  make docker-down  - Stop Docker services"
	@echo "  make docker-logs  - View Docker logs"
	@echo "  make db-shell     - Access PostgreSQL shell"
	@echo "  make clean        - Clean cache and temp files"

install:
	@echo "Installing dependencies..."
	@uv sync

start:
	@echo "Starting SynthGenie API (development)..."
	@source .env && DB_HOST=localhost uv run uvicorn synthgenie.app:app --host 0.0.0.0 --port 8000 --reload

lint:
	@echo "Running linting checks..."
	@uv run ruff check .

format:
	@echo "Formatting code..."
	@uv run ruff format .
	@uv run ruff check --fix .

typecheck:
	@echo "Running type checking..."
	@uv run pyright

docker-up:
	@echo "Starting Docker services..."
	@docker-compose up -d

docker-up-db:
	@echo "Starting Docker database service..."
	@docker-compose up -d db

docker-down:
	@echo "Stopping Docker services..."
	@docker-compose down

docker-logs:
	@echo "Viewing Docker logs..."
	@docker-compose logs -f

docker-build:
	@echo "Building Docker image..."
	@docker-compose build

db-shell:
	@echo "Accessing PostgreSQL shell..."
	@docker-compose exec db psql -U ${POSTGRES_USER:-synthgenie} -d ${POSTGRES_DB:-synthgenie}

clean:
	@echo "Cleaning cache and temporary files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".ruff_cache" -exec rm -rf {} +
	@find . -type d -name ".pyright" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name ".DS_Store" -delete
