# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Profile"]


class Profile(BaseModel):
    """Browser profile metadata."""

    id: str
    """Unique identifier for the profile"""

    created_at: datetime
    """Timestamp when the profile was created"""

    last_used_at: Optional[datetime] = None
    """Timestamp when the profile was last used"""

    name: Optional[str] = None
    """Optional, easier-to-reference name for the profile"""

    updated_at: Optional[datetime] = None
    """Timestamp when the profile was last updated"""
