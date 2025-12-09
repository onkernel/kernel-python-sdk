# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HeartbeatEvent"]


class HeartbeatEvent(BaseModel):
    """Heartbeat event sent periodically to keep SSE connection alive."""

    event: Literal["sse_heartbeat"]
    """Event type identifier (always "sse_heartbeat")."""

    timestamp: datetime
    """Time the heartbeat was sent."""
