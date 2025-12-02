# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserPoolReleaseParams"]


class BrowserPoolReleaseParams(TypedDict, total=False):
    session_id: Required[str]
    """Browser session ID to release back to the pool"""

    reuse: bool
    """Whether to reuse the browser instance or destroy it and create a new one.

    Defaults to true.
    """
