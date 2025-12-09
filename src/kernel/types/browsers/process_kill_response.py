# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ProcessKillResponse"]


class ProcessKillResponse(BaseModel):
    """Generic OK response."""

    ok: bool
    """Indicates success."""
