# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InvocationDiscoverParams"]


class InvocationDiscoverParams(TypedDict, total=False):
    login_url: str
    """Optional login page URL.

    If provided, will override the stored login URL for this discovery invocation
    and skip Phase 1 discovery.
    """
