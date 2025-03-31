from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from synthgenie.routes.agent import router as agent_router

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
