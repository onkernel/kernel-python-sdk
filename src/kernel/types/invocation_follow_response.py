# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.log_event import LogEvent
from .shared.error_detail import ErrorDetail
from .invocation_state_event import InvocationStateEvent

__all__ = ["InvocationFollowResponse", "ErrorEvent", "ErrorEventError"]


class ErrorEventError(BaseModel):
    code: str
    """Application-specific error code (machine-readable)"""

    message: str
    """Human-readable error description for debugging"""

    details: Optional[List[ErrorDetail]] = None
    """Additional error details (for multiple errors)"""

    inner_error: Optional[ErrorDetail] = None


class ErrorEvent(BaseModel):
    error: ErrorEventError

    event: Literal["error"]
    """Event type identifier (always "error")."""

    timestamp: datetime
    """Time the error occurred."""


InvocationFollowResponse: TypeAlias = Annotated[
    Union[LogEvent, InvocationStateEvent, ErrorEvent], PropertyInfo(discriminator="event")
]
