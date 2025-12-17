# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["AuthAgentInvocationCreateResponse", "AuthAgentAlreadyAuthenticated", "AuthAgentInvocationCreated"]


class AuthAgentAlreadyAuthenticated(BaseModel):
    """Response when the agent is already authenticated."""

    status: Literal["already_authenticated"]
    """Indicates the agent is already authenticated and no invocation was created."""


class AuthAgentInvocationCreated(BaseModel):
    """Response when a new invocation was created."""

    expires_at: datetime
    """When the handoff code expires."""

    handoff_code: str
    """One-time code for handoff."""

    hosted_url: str
    """URL to redirect user to."""

    invocation_id: str
    """Unique identifier for the invocation."""

    status: Literal["invocation_created"]
    """Indicates an invocation was created."""


AuthAgentInvocationCreateResponse: TypeAlias = Annotated[
    Union[AuthAgentAlreadyAuthenticated, AuthAgentInvocationCreated], PropertyInfo(discriminator="status")
]
