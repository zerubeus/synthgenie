from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        "name": "synthgenie",
        "description": "Agent tools for synthgenie",
    },
]


app = FastAPI(
    title="Synthgenie API",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
