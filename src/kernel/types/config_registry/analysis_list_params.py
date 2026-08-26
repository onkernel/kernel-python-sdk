# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AnalysisListParams"]


class AnalysisListParams(TypedDict, total=False):
    limit: int

    offset: int

    search: str
    """Case-insensitive substring search over requested URLs."""
