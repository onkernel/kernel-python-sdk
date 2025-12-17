# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReauthResponse"]


class ReauthResponse(BaseModel):
    """Response from triggering re-authentication"""

    status: Literal["reauth_started", "already_authenticated", "cannot_reauth"]
    """Result of the re-authentication attempt"""

    invocation_id: Optional[str] = None
    """ID of the re-auth invocation if one was created"""

    message: Optional[str] = None
    """Human-readable description of the result"""
