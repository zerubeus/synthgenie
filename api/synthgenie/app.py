import os
import logging
import sentry_sdk
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from synthgenie.routes.agent import router as agent_router  # noqa: E402
from synthgenie.routes.api_keys import router as api_keys_router  # noqa: E402
from synthgenie.middleware.domain_verification import (  # noqa: E402
    DomainVerificationMiddleware,
)
from synthgenie.db import engine, Base  # noqa: E402

logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

# Ensure API keys are configured
if not os.getenv("ADMIN_API_KEY"):
    import secrets

    admin_key = secrets.token_urlsafe(32)
    logger.warning("WARNING: ADMIN_API_KEY not set in environment variables.")
    logger.warning(f"Using temporary admin key for this session: {admin_key}")
    os.environ["ADMIN_API_KEY"] = admin_key

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    send_default_pii=True,
)

app = FastAPI(
    title="Synthgenie API",
    description="API for controlling Elektron Digitone synthesizer parameters",
    version="1.0.0",
)

# Allowed domains - synthgenie.com and its subdomains
allowed_origins = [
    "https://synthgenie.com",  # Main domain
    "https://www.synthgenie.com",  # www subdomain
    "https://api.synthgenie.com",  # API subdomain
    "https://chat.synthgenie.com",  # Chat subdomain
]

# For development, optionally include localhost
if os.getenv("ENVIRONMENT") == "development":
    allowed_origins.extend(
        [
            "http://localhost:3000",
            "http://localhost:8000",
        ]
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["X-API-Key", "Content-Type", "Authorization"],
    allow_credentials=True,
)

# Add domain verification middleware
root_domain = "synthgenie.com"
app.add_middleware(DomainVerificationMiddleware, allowed_domains=[root_domain])

# Include routers
app.include_router(agent_router)
app.include_router(api_keys_router)
