# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentAuthRunResponse"]


class AgentAuthRunResponse(BaseModel):
    app_name: str
    """App name (org name at time of run creation)"""

    expires_at: datetime
    """When the handoff code expires"""

    status: Literal["ACTIVE", "ENDED", "EXPIRED", "CANCELED"]
    """Run status"""

    target_domain: str
    """Target domain for authentication"""
