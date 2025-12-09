# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserPersistenceParam"]


class BrowserPersistenceParam(TypedDict, total=False):
    """DEPRECATED: Use timeout_seconds (up to 72 hours) and Profiles instead."""

    id: Required[str]
    """DEPRECATED: Unique identifier for the persistent browser session."""
