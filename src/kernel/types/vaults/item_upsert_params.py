# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .card_vault_item_spec_param import CardVaultItemSpecParam
from .wallet_vault_item_spec_param import WalletVaultItemSpecParam

__all__ = ["ItemUpsertParams", "WalletVaultItemRequest", "CardVaultItemRequest"]


class WalletVaultItemRequest(TypedDict, total=False):
    id_or_name: Required[str]

    spec: Required[WalletVaultItemSpecParam]
    """AgentCard wallet.

    Mode (sandbox vs live) is fixed by the deployment's AgentCard credential; there
    is no per-item test flag. user_id may only reference a user already enrolled by
    a wallet in this organization.
    """

    type: Required[Literal["wallet"]]


class CardVaultItemRequest(TypedDict, total=False):
    id_or_name: Required[str]

    spec: Required[CardVaultItemSpecParam]
    """Live payment card. Test-mode card creation is not supported."""

    type: Required[Literal["card"]]


ItemUpsertParams: TypeAlias = Union[WalletVaultItemRequest, CardVaultItemRequest]
