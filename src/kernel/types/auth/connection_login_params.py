# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..browsers.browser_telemetry_categories_config_param import BrowserTelemetryCategoriesConfigParam

__all__ = ["ConnectionLoginParams", "BrowserTelemetry", "Proxy"]


class ConnectionLoginParams(TypedDict, total=False):
    browser_telemetry: Optional[BrowserTelemetry]
    """Override the connection's default browser telemetry configuration for this
    login.

    When omitted, the connection's browser_telemetry default is used. Uses the exact
    create-browser configuration.
    """

    proxy: Proxy
    """Proxy selection.

    Provide either id or name. The proxy must be in the same project as the resource
    referencing it. When selecting by name, the name must match exactly one active
    proxy in the project. Ambiguous names return a 400; use id for stable
    references.
    """

    record_session: bool
    """Override the connection's default for recording this login's browser session.

    When omitted, the connection's record_session default is used.
    """


class BrowserTelemetry(TypedDict, total=False):
    """Override the connection's default browser telemetry configuration for this login.

    When omitted, the connection's browser_telemetry default is used. Uses the exact create-browser configuration.
    """

    browser: BrowserTelemetryCategoriesConfigParam
    """Per-category capture flags.

    The operational categories (control, connection, system, captcha) are captured
    whenever telemetry is enabled; set one to enabled=false to opt out. The CDP
    categories (console, network, page, interaction) and screenshot are off by
    default; set enabled=true to opt in. On create, provided categories layer onto
    the default set. On update, provided categories merge onto the session's current
    config; when no telemetry is active this falls back to the default set (matching
    create). If browser is omitted or empty, the default set is used. A browser
    config that disables every category stops capture on update and starts no
    capture on create.
    """

    enabled: bool
    """Request shortcut for browser telemetry capture.

    True enables capture; with no browser category settings it captures the default
    set (control, connection, system, captcha), and any browser category settings
    are layered onto that default set. On update, enabled=true resolves the config
    fresh from the default set plus any provided categories, replacing the session's
    current selection rather than merging onto it; omit enabled to merge categories
    onto the current selection instead. False stops capture on update and starts no
    capture on create. enabled=false cannot be combined with browser category
    settings.
    """


class Proxy(TypedDict, total=False):
    """Proxy selection.

    Provide either id or name. The proxy must be in the same project as the resource referencing it.
    When selecting by name, the name must match exactly one active proxy in the project. Ambiguous names return a 400; use id for stable references.
    """

    id: str
    """Proxy ID"""

    name: str
    """Proxy name"""
