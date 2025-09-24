# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .browser_persistence_param import BrowserPersistenceParam

__all__ = ["BrowserCreateParams", "Profile"]


class BrowserCreateParams(TypedDict, total=False):
    headless: bool
    """If true, launches the browser using a headless image (no VNC/GUI).

    Defaults to false.
    """

    invocation_id: str
    """action invocation ID"""

    persistence: BrowserPersistenceParam
    """Optional persistence configuration for the browser session."""

    profile: Profile
    """Profile selection for the browser session.

    Provide either id or name. If specified, the matching profile will be loaded
    into the browser session. Profiles must be created beforehand.
    """

    proxy_id: str
    """Optional proxy to associate to the browser session.

    Must reference a proxy belonging to the caller's org.
    """

    stealth: bool
    """
    If true, launches the browser in stealth mode to reduce detection by anti-bot
    mechanisms.
    """

    timeout_seconds: int
    """The number of seconds of inactivity before the browser session is terminated.

    Only applicable to non-persistent browsers. Activity includes CDP connections
    and live view connections. Defaults to 60 seconds. Minimum allowed is 10
    seconds. Maximum allowed is 86400 (24 hours). We check for inactivity every 5
    seconds, so the actual timeout behavior you will see is +/- 5 seconds around the
    specified value.
    """


class Profile(TypedDict, total=False):
    id: str
    """Profile ID to load for this browser session"""

    name: str
    """Profile name to load for this browser session (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
    """

    save_changes: bool
    """
    If true, save changes made during the session back to the profile when the
    session ends.
    """
