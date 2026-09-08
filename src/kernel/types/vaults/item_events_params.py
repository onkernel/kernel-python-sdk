# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ItemEventsParams"]


class ItemEventsParams(TypedDict, total=False):
    id_or_name: Required[str]

    after: str
    """Return events after this event ID."""

    wait: int
    """Long-poll for new events for up to this many seconds."""
