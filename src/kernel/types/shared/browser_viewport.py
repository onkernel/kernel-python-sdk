# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserViewport"]


class BrowserViewport(BaseModel):
    height: int
    """Browser window height in pixels."""

    width: int
    """Browser window width in pixels."""

    refresh_rate: Optional[int] = None
    """Display refresh rate in Hz.

    If omitted, automatically determined from width and height.
    """
