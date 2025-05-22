# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrowserRetrieveResponse", "Persistence"]


class Persistence(BaseModel):
    id: str
    """Unique identifier for the persistent browser session."""


class BrowserRetrieveResponse(BaseModel):
    browser_live_view_url: str
    """Remote URL for live viewing the browser session"""

    cdp_ws_url: str
    """Websocket URL for Chrome DevTools Protocol connections to the browser session"""

    session_id: str
    """Unique identifier for the browser session"""

    persistence: Optional[Persistence] = None
    """Optional persistence configuration for the browser session."""
