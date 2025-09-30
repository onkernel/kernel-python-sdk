# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .profile import Profile
from .._models import BaseModel
from .browser_persistence import BrowserPersistence

__all__ = ["BrowserCreateResponse"]


class BrowserCreateResponse(BaseModel):
    cdp_ws_url: str
    """Websocket URL for Chrome DevTools Protocol connections to the browser session"""

    created_at: datetime
    """When the browser session was created."""

    headless: bool
    """Whether the browser session is running in headless mode."""

    session_id: str
    """Unique identifier for the browser session"""

    stealth: bool
    """Whether the browser session is running in stealth mode."""

    timeout_seconds: int
    """The number of seconds of inactivity before the browser session is terminated."""

    browser_live_view_url: Optional[str] = None
    """Remote URL for live viewing the browser session.

    Only available for non-headless browsers.
    """

    persistence: Optional[BrowserPersistence] = None
    """Optional persistence configuration for the browser session."""

    profile: Optional[Profile] = None
    """Browser profile metadata."""

    proxy_id: Optional[str] = None
    """ID of the proxy associated with this browser session, if any."""
