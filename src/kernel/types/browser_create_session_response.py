# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BrowserCreateSessionResponse"]


class BrowserCreateSessionResponse(BaseModel):
    cdp_ws_url: str
    """Websocket URL for Chrome DevTools Protocol connections to the browser session"""

    remote_url: str
    """Remote URL for live viewing the browser session"""

    session_id: str = FieldInfo(alias="sessionId")
    """Unique identifier for the browser session"""
