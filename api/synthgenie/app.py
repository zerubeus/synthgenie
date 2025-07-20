import logging
import os

import logfire
import sentry_sdk
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from synthgenie.auth.routes import router as api_keys_router
from synthgenie.db.connection import initialize_db
from synthgenie.synthesizers.digitone.routes import router as digitone_router
from synthgenie.synthesizers.sub37.routes import router as sub37_router

load_dotenv()

logger = logging.getLogger(__name__)

logfire.configure(token=os.getenv('LOGFIRE_TOKEN'))

# Initialize database
initialize_db()

# Ensure API keys are configured
if not os.getenv('ADMIN_API_KEY'):
    import secrets

    admin_key = secrets.token_urlsafe(32)
    logger.warning('WARNING: ADMIN_API_KEY not set in environment variables.')
    logger.warning(f'Using temporary admin key for this session: {admin_key}')
    os.environ['ADMIN_API_KEY'] = admin_key

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    send_default_pii=True,
)

app = FastAPI(
    title='Synthgenie API',
    description='API for controlling Elektron Digitone synthesizer parameters',
    version='1.0.0',
)

# Get base URL from environment
base_url = os.getenv('BASE_URL', 'synthgenie.com')

# Allowed domains - base_url and its subdomains
allowed_origins = [
    f'https://{base_url}',  # Main domain
    f'https://www.{base_url}',  # www subdomain
    f'https://api.{base_url}',  # API subdomain
    f'https://chat.{base_url}',  # Chat subdomain
]

# For development, optionally include localhost
if os.getenv('API_ENV') == 'development':
    allowed_origins.extend(
        [
            'http://localhost:3000',
            'http://localhost:5173',
            'http://localhost:8000',
        ]
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=['GET', 'POST', 'DELETE', 'PUT'],
    allow_headers=['X-API-Key', 'Content-Type', 'Authorization'],
    allow_credentials=True,
)

# Add TrustedHostMiddleware instead of custom domain verification
# Skip host validation in development if specified
if os.getenv('SKIP_DOMAIN_CHECK') != 'true':
    allowed_hosts = [base_url, f'*.{base_url}']

    # Add localhost patterns for development
    if os.getenv('ENVIRONMENT') == 'development':
        allowed_hosts.extend(['localhost', '127.0.0.1'])

    app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)

# Include routers
app.include_router(digitone_router)
app.include_router(sub37_router)
app.include_router(api_keys_router)
