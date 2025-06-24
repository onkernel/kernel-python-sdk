# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..shared.log_event import LogEvent
from ..shared.heartbeat_event import HeartbeatEvent

__all__ = ["DeploymentFollowResponse", "StateEvent", "StateUpdateEvent"]


class StateEvent(BaseModel):
    event: Literal["state"]
    """Event type identifier (always "state")."""

    state: str
    """
    Current application state (e.g., "deploying", "running", "succeeded", "failed").
    """

    timestamp: Optional[datetime] = None
    """Time the state was reported."""


class StateUpdateEvent(BaseModel):
    event: Literal["state_update"]
    """Event type identifier (always "state_update")."""

    state: str
    """New application state (e.g., "running", "succeeded", "failed")."""

    timestamp: Optional[datetime] = None
    """Time the state change occurred."""


DeploymentFollowResponse: TypeAlias = Annotated[
    Union[StateEvent, StateUpdateEvent, LogEvent, HeartbeatEvent], PropertyInfo(discriminator="event")
]
