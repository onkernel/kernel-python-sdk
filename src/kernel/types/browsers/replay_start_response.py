# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ReplayStartResponse"]


class ReplayStartResponse(BaseModel):
    replay_id: str
    """Unique identifier for the replay recording."""

    finished_at: Optional[datetime] = None
    """Timestamp when replay finished"""

    replay_view_url: Optional[str] = None
    """URL for viewing the replay recording."""

    started_at: Optional[datetime] = None
    """Timestamp when replay started"""
