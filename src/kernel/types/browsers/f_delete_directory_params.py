# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FDeleteDirectoryParams"]


class FDeleteDirectoryParams(TypedDict, total=False):
    path: Required[str]
    """Absolute path to delete."""
