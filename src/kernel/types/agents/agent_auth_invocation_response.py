# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentAuthInvocationResponse"]


class AgentAuthInvocationResponse(BaseModel):
    """Response from get invocation endpoint"""

    app_name: str
    """App name (org name at time of invocation creation)"""

    expires_at: datetime
    """When the handoff code expires"""

    status: Literal["IN_PROGRESS", "SUCCESS", "EXPIRED", "CANCELED"]
    """Invocation status"""

    target_domain: str
    """Target domain for authentication"""
