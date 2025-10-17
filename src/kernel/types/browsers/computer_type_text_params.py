# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ComputerTypeTextParams"]


class ComputerTypeTextParams(TypedDict, total=False):
    text: Required[str]
    """Text to type on the browser instance"""

    delay: int
    """Delay in milliseconds between keystrokes"""
