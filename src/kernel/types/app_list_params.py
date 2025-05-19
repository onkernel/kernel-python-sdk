# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    app_name: str
    """Filter results by application name."""

    version: str
    """Filter results by version label."""
