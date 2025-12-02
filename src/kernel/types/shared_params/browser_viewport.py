# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserViewport"]


class BrowserViewport(TypedDict, total=False):
    height: Required[int]
    """Browser window height in pixels."""

    width: Required[int]
    """Browser window width in pixels."""

    refresh_rate: int
    """Display refresh rate in Hz.

    If omitted, automatically determined from width and height.
    """
