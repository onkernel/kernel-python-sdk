# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["AgentAuthStartResponse"]


class AgentAuthStartResponse(BaseModel):
    expires_at: datetime
    """When the handoff code expires"""

    handoff_code: str
    """One-time code for handoff"""

    hosted_url: str
    """URL to redirect user to"""

    run_id: str
    """Unique identifier for the run"""
