# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .browser_proxy_mode import BrowserProxyMode

__all__ = ["BrowserProxy"]


class BrowserProxy(BaseModel):
    """Resolved proxy configuration for a browser session.

    Selected proxies are returned by stable ID.
    """

    id: Optional[str] = None
    """Selected proxy ID."""

    mode: Optional[BrowserProxyMode] = None
    """Proxy egress mode.

    direct forces no proxy regardless of stealth. default uses the browser's
    stealth-derived default: Kernel's default stealth proxy when stealth=true, or
    direct egress when stealth=false. default is primarily useful on browser update
    to restore the browser default after selected-proxy egress.
    """

    name: Optional[str] = None
    """Selected proxy name."""
