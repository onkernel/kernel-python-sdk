# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FMoveParams"]


class FMoveParams(TypedDict, total=False):
    dest_path: Required[str]
    """Absolute destination path."""

    src_path: Required[str]
    """Absolute source path."""
