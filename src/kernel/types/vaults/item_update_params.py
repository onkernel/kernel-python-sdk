# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .card_vault_item_spec_param import CardVaultItemSpecParam

__all__ = ["ItemUpdateParams"]


class ItemUpdateParams(TypedDict, total=False):
    id_or_name: Required[str]

    spec: Required[CardVaultItemSpecParam]
    """Live payment card. Test-mode card creation is not supported."""
