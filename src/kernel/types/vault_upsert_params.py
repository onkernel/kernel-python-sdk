# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VaultUpsertParams"]


class VaultUpsertParams(TypedDict, total=False):
    name: Required[str]
    """Immutable name used to create or retrieve the vault."""
