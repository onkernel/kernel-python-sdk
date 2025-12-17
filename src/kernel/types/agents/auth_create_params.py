# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthCreateParams", "Proxy"]


class AuthCreateParams(TypedDict, total=False):
    profile_name: Required[str]
    """Name of the profile to use for this auth agent"""

    target_domain: Required[str]
    """Target domain for authentication"""

    credential_name: str
    """Optional name of an existing credential to use for this auth agent.

    If provided, the credential will be linked to the agent and its values will be
    used to auto-fill the login form on invocation.
    """

    login_url: str
    """Optional login page URL.

    If provided, will be stored on the agent and used to skip discovery in future
    invocations.
    """

    proxy: Proxy
    """Optional proxy configuration"""


class Proxy(TypedDict, total=False):
    """Optional proxy configuration"""

    proxy_id: str
    """ID of the proxy to use"""
