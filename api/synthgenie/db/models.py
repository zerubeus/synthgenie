from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from uuid import uuid4

from synthgenie.db import Base


def generate_uuid():
    """Generate a UUID string."""
    return str(uuid4())


class ApiKey(Base):
    """API key model."""

    __tablename__ = "api_keys"

    # The API key itself serves as the primary key
    key = Column(String, primary_key=True, index=True, default=generate_uuid)
    user_id = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<ApiKey(user_id='{self.user_id}')>"
