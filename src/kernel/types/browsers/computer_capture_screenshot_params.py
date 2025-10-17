# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ComputerCaptureScreenshotParams", "Region"]


class ComputerCaptureScreenshotParams(TypedDict, total=False):
    region: Region


class Region(TypedDict, total=False):
    height: Required[int]
    """Height of the region in pixels"""

    width: Required[int]
    """Width of the region in pixels"""

    x: Required[int]
    """X coordinate of the region's top-left corner"""

    y: Required[int]
    """Y coordinate of the region's top-left corner"""
