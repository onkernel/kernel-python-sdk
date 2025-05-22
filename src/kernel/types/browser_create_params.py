# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserCreateParams", "Persistence"]


class BrowserCreateParams(TypedDict, total=False):
    invocation_id: Required[str]
    """action invocation ID"""

    persistence: Persistence
    """Optional persistence configuration for the browser session."""


class Persistence(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the persistent browser session."""
