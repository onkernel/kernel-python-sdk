# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FSetFilePermissionsParams"]


class FSetFilePermissionsParams(TypedDict, total=False):
    mode: Required[str]
    """File mode bits (octal string, e.g. 644)."""

    path: Required[str]
    """Absolute path whose permissions are to be changed."""

    group: str
    """New group name or GID."""

    owner: str
    """New owner username or UID."""
