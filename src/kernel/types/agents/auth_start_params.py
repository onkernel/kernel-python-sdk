# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthStartParams", "Proxy"]


class AuthStartParams(TypedDict, total=False):
    profile_name: Required[str]
    """Name of the profile to use for this flow"""

    target_domain: Required[str]
    """Target domain for authentication"""

    app_logo_url: str
    """Optional logo URL for the application"""

    login_url: str
    """Optional login page URL.

    If provided, will be stored on the agent and used to skip Phase 1 discovery in
    future invocations.
    """

    proxy: Proxy
    """Optional proxy configuration"""


class Proxy(TypedDict, total=False):
    proxy_id: str
    """ID of the proxy to use"""
