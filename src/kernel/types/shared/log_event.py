# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LogEvent"]


class LogEvent(BaseModel):
    event: Literal["log"]
    """Event type identifier (always "log")."""

    message: str
    """Log message text."""

    timestamp: datetime
    """Time the log entry was produced."""
