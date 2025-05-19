# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "DeploymentFollowResponse",
    "DeploymentFollowResponseItem",
    "DeploymentFollowResponseItemStateEvent",
    "DeploymentFollowResponseItemStateUpdateEvent",
    "DeploymentFollowResponseItemLogEvent",
]


class DeploymentFollowResponseItemStateEvent(BaseModel):
    event: Literal["state"]
    """Event type identifier (always "state")."""

    state: str
    """
    Current application state (e.g., "deploying", "running", "succeeded", "failed").
    """

    timestamp: Optional[datetime] = None
    """Time the state was reported."""


class DeploymentFollowResponseItemStateUpdateEvent(BaseModel):
    event: Literal["state_update"]
    """Event type identifier (always "state_update")."""

    state: str
    """New application state (e.g., "running", "succeeded", "failed")."""

    timestamp: Optional[datetime] = None
    """Time the state change occurred."""


class DeploymentFollowResponseItemLogEvent(BaseModel):
    event: Literal["log"]
    """Event type identifier (always "log")."""

    message: str
    """Log message text."""

    timestamp: Optional[datetime] = None
    """Time the log entry was produced."""


DeploymentFollowResponseItem: TypeAlias = Annotated[
    Union[
        DeploymentFollowResponseItemStateEvent,
        DeploymentFollowResponseItemStateUpdateEvent,
        DeploymentFollowResponseItemLogEvent,
    ],
    PropertyInfo(discriminator="event"),
]

DeploymentFollowResponse: TypeAlias = List[DeploymentFollowResponseItem]
