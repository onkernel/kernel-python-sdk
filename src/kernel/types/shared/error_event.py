# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .error import Error
from ..._models import BaseModel

__all__ = ["ErrorEvent"]


class ErrorEvent(BaseModel):
    error: Error

    event: Literal["error"]
    """Event type identifier (always "error")."""

    timestamp: datetime
    """Time the error occurred."""
