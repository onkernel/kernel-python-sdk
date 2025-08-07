# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FWriteFileParams"]


class FWriteFileParams(TypedDict, total=False):
    path: Required[str]
    """Destination absolute file path."""

    mode: str
    """Optional file mode (octal string, e.g. 644). Defaults to 644."""
