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

    timestamp: Optional[datetime] = None
    """Time the log entry was produced."""


class DeploymentStateEventDeployment(BaseModel):
    id: str
    """Unique identifier for the deployment"""

    created_at: datetime
    """Timestamp when the deployment was created"""

    region: str
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

    timestamp: Optional[datetime] = None
    """Time the state was reported."""


class AppVersionSummaryEvent(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the app version"""

    app_name: Optional[str] = None
    """Name of the application"""

    env_vars: Optional[Dict[str, str]] = None
    """Environment variables configured for this app version"""

    event: Optional[Literal["app_version_summary"]] = None
    """Event type identifier (always "app_version_summary")."""

    region: Optional[str] = None
    """Deployment region code"""

    version: Optional[str] = None
    """Version label for the application"""


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
    error: Optional[ErrorEventError] = None

    event: Optional[Literal["error"]] = None
    """Event type identifier (always "error")."""


DeploymentFollowResponse: TypeAlias = Annotated[
    Union[LogEvent, DeploymentStateEvent, AppVersionSummaryEvent, ErrorEvent], PropertyInfo(discriminator="event")
]
