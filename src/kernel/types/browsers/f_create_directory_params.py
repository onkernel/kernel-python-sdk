# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FCreateDirectoryParams"]


class FCreateDirectoryParams(TypedDict, total=False):
    path: Required[str]
    """Absolute directory path to create."""

    mode: str
    """Optional directory mode (octal string, e.g. 755). Defaults to 755."""
