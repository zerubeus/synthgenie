from typing import List, Optional
from sqlalchemy.orm import Session
import secrets

from synthgenie.db.models import ApiKey


def create_api_key(db: Session, user_id: str) -> ApiKey:
    """
    Create a new API key for a user.

    Args:
        db: Database session
        user_id: User ID to associate with the API key

    Returns:
        The created API key
    """
    # Generate a secure API key
    api_key_value = secrets.token_urlsafe(32)

    # Create the API key in the database
    api_key = ApiKey(key=api_key_value, user_id=user_id)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return api_key


def get_api_key(db: Session, key: str) -> Optional[ApiKey]:
    """
    Get an API key by its value.

    Args:
        db: Database session
        key: API key value

    Returns:
        The API key if found, None otherwise
    """
    return db.query(ApiKey).filter(ApiKey.key == key).first()


def get_user_api_keys(db: Session, user_id: str) -> List[ApiKey]:
    """
    Get all API keys for a user.

    Args:
        db: Database session
        user_id: User ID

    Returns:
        List of API keys for the user
    """
    return db.query(ApiKey).filter(ApiKey.user_id == user_id).all()


def delete_api_key(db: Session, key: str) -> bool:
    """
    Delete an API key.

    Args:
        db: Database session
        key: API key value

    Returns:
        True if the key was deleted, False otherwise
    """
    api_key = get_api_key(db, key)
    if api_key:
        db.delete(api_key)
        db.commit()
        return True
    return False
