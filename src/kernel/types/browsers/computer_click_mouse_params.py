# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ComputerClickMouseParams"]


class ComputerClickMouseParams(TypedDict, total=False):
    x: Required[int]
    """X coordinate of the click position"""

    y: Required[int]
    """Y coordinate of the click position"""

    button: Literal["left", "right", "middle", "back", "forward"]
    """Mouse button to interact with"""

    click_type: Literal["down", "up", "click"]
    """Type of click action"""

    hold_keys: SequenceNotStr[str]
    """Modifier keys to hold during the click"""

    num_clicks: int
    """Number of times to repeat the click"""
