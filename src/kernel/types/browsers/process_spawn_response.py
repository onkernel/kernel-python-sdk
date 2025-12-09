# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProcessSpawnResponse"]


class ProcessSpawnResponse(BaseModel):
    """Information about a spawned process."""

    pid: Optional[int] = None
    """OS process ID."""

    process_id: Optional[str] = None
    """Server-assigned identifier for the process."""

    started_at: Optional[datetime] = None
    """Timestamp when the process started."""
