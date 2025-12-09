# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .browser_pool_request import BrowserPoolRequest

__all__ = ["BrowserPool"]


class BrowserPool(BaseModel):
    """A browser pool containing multiple identically configured browsers."""

    id: str
    """Unique identifier for the browser pool"""

    acquired_count: int
    """Number of browsers currently acquired from the pool"""

    available_count: int
    """Number of browsers currently available in the pool"""

    browser_pool_config: BrowserPoolRequest
    """Configuration used to create all browsers in this pool"""

    created_at: datetime
    """Timestamp when the browser pool was created"""

    name: Optional[str] = None
    """Browser pool name, if set"""
