# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["WatchStartResponse"]


class WatchStartResponse(BaseModel):
    watch_id: Optional[str] = None
    """Unique identifier for the directory watch"""
