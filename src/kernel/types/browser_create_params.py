# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .browser_persistence_param import BrowserPersistenceParam

__all__ = ["BrowserCreateParams", "Extension", "Profile", "Viewport"]


class BrowserCreateParams(TypedDict, total=False):
    extensions: Iterable[Extension]
    """List of browser extensions to load into the session.

    Provide each by id or name.
    """

    headless: bool
    """If true, launches the browser using a headless image (no VNC/GUI).

    Defaults to false.
    """

    invocation_id: str
    """action invocation ID"""

    kiosk_mode: bool
    """
    If true, launches the browser in kiosk mode to hide address bar and tabs in live
    view.
    """

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

    viewport: Viewport
    """Initial browser window size in pixels with optional refresh rate.

    If omitted, image defaults apply (commonly 1024x768@60). Only specific viewport
    configurations are supported. The server will reject unsupported combinations.
    Supported resolutions are: 2560x1440@10, 1920x1080@25, 1920x1200@25,
    1440x900@25, 1024x768@60 If refresh_rate is not provided, it will be
    automatically determined from the width and height if they match a supported
    configuration exactly. Note: Higher resolutions may affect the responsiveness of
    live view browser
    """


class Extension(TypedDict, total=False):
    id: str
    """Extension ID to load for this browser session"""

    name: str
    """Extension name to load for this browser session (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
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


class Viewport(TypedDict, total=False):
    height: Required[int]
    """Browser window height in pixels."""

    width: Required[int]
    """Browser window width in pixels."""

    refresh_rate: int
    """Display refresh rate in Hz.

    If omitted, automatically determined from width and height.
    """
