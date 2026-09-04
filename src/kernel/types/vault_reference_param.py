# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VaultReferenceParam"]


class VaultReferenceParam(TypedDict, total=False):
    """Reference to a project-scoped vault. Provide exactly one of id or name."""

    id: str

    name: str
