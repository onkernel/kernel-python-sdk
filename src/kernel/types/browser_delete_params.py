# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrowserDeleteParams"]


class BrowserDeleteParams(TypedDict, total=False):
    persistent_id: Required[str]
    """Persistent browser identifier"""
