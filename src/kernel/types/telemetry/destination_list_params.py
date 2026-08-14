# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DestinationListParams"]


class DestinationListParams(TypedDict, total=False):
    limit: int
    """Limit the number of destinations to return."""

    name: str
    """Exact-match filter on destination name using the database collation.

    In production, matching is case- and accent-insensitive.
    """

    offset: int
    """Offset the number of destinations to return."""

    query: str
    """Case-insensitive substring match against destination name or endpoint.

    IDs match by exact value.
    """
