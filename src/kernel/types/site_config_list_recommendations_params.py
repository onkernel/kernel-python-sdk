# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SiteConfigListRecommendationsParams"]


class SiteConfigListRecommendationsParams(TypedDict, total=False):
    limit: int

    offset: int

    sort_by: Literal["target", "recommended_config", "last_requested_at", "success_rate"]

    sort_order: Literal["asc", "desc"]
