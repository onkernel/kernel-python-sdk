# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserListParams"]


class BrowserListParams(TypedDict, total=False):
    include_deleted: bool
    """
    When true, includes soft-deleted browser sessions in the results alongside
    active sessions.
    """

    limit: int
    """Maximum number of results to return. Defaults to 20, maximum 100."""

    offset: int
    """Number of results to skip. Defaults to 0."""
