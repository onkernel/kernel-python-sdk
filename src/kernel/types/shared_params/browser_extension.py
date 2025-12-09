# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserExtension"]


class BrowserExtension(TypedDict, total=False):
    """Extension selection for the browser session.

    Provide either id or name of an extension uploaded to Kernel.
    """

    id: str
    """Extension ID to load for this browser session"""

    name: str
    """Extension name to load for this browser session (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
    """
