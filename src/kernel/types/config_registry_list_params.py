# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConfigRegistryListParams"]


class ConfigRegistryListParams(TypedDict, total=False):
    limit: int

    offset: int

    search: str
    """
    Case-insensitive substring search over normalized targets, including domain,
    subdomain, and path.
    """

    sort_by: Literal["target", "analysis_status", "recommended_config", "last_requested_at", "success_rate"]

    sort_order: Literal["asc", "desc"]
