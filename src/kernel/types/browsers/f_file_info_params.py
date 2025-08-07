# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FFileInfoParams"]


class FFileInfoParams(TypedDict, total=False):
    path: Required[str]
    """Absolute path of the file or directory."""
