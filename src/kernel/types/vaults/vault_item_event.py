# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VaultItemEvent"]


class VaultItemEvent(BaseModel):
    id: str

    created_at: datetime

    name: str

    browser_id: Optional[str] = None
    """Browser session associated with the event, when applicable."""

    data: Optional[Dict[str, object]] = None
