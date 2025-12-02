# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserPoolDeleteParams"]


class BrowserPoolDeleteParams(TypedDict, total=False):
    force: bool
    """If true, force delete even if browsers are currently leased.

    Leased browsers will be terminated.
    """
