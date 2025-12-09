# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .error_model import ErrorModel

__all__ = ["ErrorEvent"]


class ErrorEvent(BaseModel):
    """An error event from the application."""

    error: ErrorModel

    event: Literal["error"]
    """Event type identifier (always "error")."""

    timestamp: datetime
    """Time the error occurred."""
