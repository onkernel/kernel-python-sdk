# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WatchStartParams"]


class WatchStartParams(TypedDict, total=False):
    path: Required[str]
    """Directory to watch."""

    recursive: bool
    """Whether to watch recursively."""
