import os
import sentry_sdk
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from synthgenie.routes.agent import router as agent_router  # noqa: E402

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    send_default_pii=True,
)

app = FastAPI(
    title="Synthgenie API",
    description="API for controlling Elektron Digitone synthesizer parameters",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Include routers
app.include_router(agent_router)
