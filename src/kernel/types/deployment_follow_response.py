# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "DeploymentFollowResponse",
    "LogEvent",
    "DeploymentStateEvent",
    "DeploymentStateEventDeployment",
    "AppVersionSummaryEvent",
    "ErrorEvent",
    "ErrorEventError",
    "ErrorEventErrorDetail",
    "ErrorEventErrorInnerError",
]


class LogEvent(BaseModel):
    event: Literal["log"]
    """Event type identifier (always "log")."""

    message: str
    """Log message text."""

    timestamp: datetime
    """Time the log entry was produced."""


class DeploymentStateEventDeployment(BaseModel):
    id: str
    """Unique identifier for the deployment"""

    created_at: datetime
    """Timestamp when the deployment was created"""

    region: Literal["aws.us-east-1a"]
    """Deployment region code"""

    status: Literal["queued", "in_progress", "running", "failed", "stopped"]
    """Current status of the deployment"""

    entrypoint_rel_path: Optional[str] = None
    """Relative path to the application entrypoint"""

    env_vars: Optional[Dict[str, str]] = None
    """Environment variables configured for this deployment"""

    status_reason: Optional[str] = None
    """Status reason"""

    updated_at: Optional[datetime] = None
    """Timestamp when the deployment was last updated"""


class DeploymentStateEvent(BaseModel):
    deployment: DeploymentStateEventDeployment
    """Deployment record information."""

    event: Literal["deployment_state"]
    """Event type identifier (always "deployment_state")."""

    timestamp: datetime
    """Time the state was reported."""


class AppVersionSummaryEvent(BaseModel):
    id: str
    """Unique identifier for the app version"""

    actions: List[str]
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


class ErrorEventErrorDetail(BaseModel):
    code: Optional[str] = None
    """Lower-level error code providing more specific detail"""

    message: Optional[str] = None
    """Further detail about the error"""


class ErrorEventErrorInnerError(BaseModel):
    code: Optional[str] = None
    """Lower-level error code providing more specific detail"""

    message: Optional[str] = None
    """Further detail about the error"""


class ErrorEventError(BaseModel):
    code: str
    """Application-specific error code (machine-readable)"""

    message: str
    """Human-readable error description for debugging"""

    details: Optional[List[ErrorEventErrorDetail]] = None
    """Additional error details (for multiple errors)"""

    inner_error: Optional[ErrorEventErrorInnerError] = None


class ErrorEvent(BaseModel):
    error: ErrorEventError

    event: Literal["error"]
    """Event type identifier (always "error")."""

    timestamp: datetime
    """Time the error occurred."""


DeploymentFollowResponse: TypeAlias = Annotated[
    Union[LogEvent, DeploymentStateEvent, AppVersionSummaryEvent, ErrorEvent], PropertyInfo(discriminator="event")
]
