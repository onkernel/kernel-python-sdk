# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.log_event import LogEvent
from .shared.error_detail import ErrorDetail
from .deployment_state_event import DeploymentStateEvent

__all__ = [
    "DeploymentFollowResponse",
    "AppVersionSummaryEvent",
    "AppVersionSummaryEventAction",
    "ErrorEvent",
    "ErrorEventError",
]


class AppVersionSummaryEventAction(BaseModel):
    name: str
    """Name of the action"""


class AppVersionSummaryEvent(BaseModel):
    id: str
    """Unique identifier for the app version"""

    actions: List[AppVersionSummaryEventAction]
    """List of actions available on the app"""

    app_name: str
    """Name of the application"""

    event: Literal["app_version_summary"]
    """Event type identifier (always "app_version_summary")."""

    region: Literal["aws.us-east-1a"]
    """Deployment region code"""

    timestamp: datetime
    """Time the state was reported."""

    version: str
    """Version label for the application"""

    env_vars: Optional[Dict[str, str]] = None
    """Environment variables configured for this app version"""


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


DeploymentFollowResponse: TypeAlias = Annotated[
    Union[LogEvent, DeploymentStateEvent, AppVersionSummaryEvent, ErrorEvent], PropertyInfo(discriminator="event")
]
