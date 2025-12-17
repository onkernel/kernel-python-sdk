# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvocationCreateParams"]


class InvocationCreateParams(TypedDict, total=False):
    auth_agent_id: Required[str]
    """ID of the auth agent to create an invocation for"""

    save_credential_as: str
    """
    If provided, saves the submitted credentials under this name upon successful
    login. The credential will be linked to the auth agent for automatic
    re-authentication.
    """
