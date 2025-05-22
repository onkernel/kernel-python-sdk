# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .browser_persistence_param import BrowserPersistenceParam

__all__ = ["BrowserCreateParams"]


class BrowserCreateParams(TypedDict, total=False):
    invocation_id: Required[str]
    """action invocation ID"""

    persistence: BrowserPersistenceParam
    """Optional persistence configuration for the browser session."""
