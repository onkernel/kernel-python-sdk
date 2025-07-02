# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .browser_persistence_param import BrowserPersistenceParam

__all__ = ["BrowserCreateParams"]


class BrowserCreateParams(TypedDict, total=False):
    headless: bool
    """If true, launches the browser using a headless image (no VNC/GUI).

    Defaults to false.
    """

    invocation_id: str
    """action invocation ID"""

    persistence: BrowserPersistenceParam
    """Optional persistence configuration for the browser session."""

    stealth: bool
    """
    If true, launches the browser in stealth mode to reduce detection by anti-bot
    mechanisms.
    """
