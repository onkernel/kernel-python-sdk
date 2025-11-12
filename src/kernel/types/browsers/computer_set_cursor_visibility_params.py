# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ComputerSetCursorVisibilityParams"]


class ComputerSetCursorVisibilityParams(TypedDict, total=False):
    hidden: Required[bool]
    """Whether the cursor should be hidden or visible"""
