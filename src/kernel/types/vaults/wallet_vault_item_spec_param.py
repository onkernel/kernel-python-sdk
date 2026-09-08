# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "WalletVaultItemSpecParam",
    "LinkWalletVaultItemSpec",
    "LinkWalletVaultItemSpecAuthorization",
    "LinkWalletVaultItemSpecAuthorizationClient",
    "AgentCardWalletVaultItemSpec",
]


class LinkWalletVaultItemSpecAuthorizationClient(TypedDict, total=False):
    type: Required[Literal["kernel_managed"]]


class LinkWalletVaultItemSpecAuthorization(TypedDict, total=False):
    client: Required[LinkWalletVaultItemSpecAuthorizationClient]

    method: Required[Literal["oauth"]]


class LinkWalletVaultItemSpec(TypedDict, total=False):
    authorization: Required[LinkWalletVaultItemSpecAuthorization]

    provider: Required[Literal["link"]]


class AgentCardWalletVaultItemSpec(TypedDict, total=False):
    """AgentCard wallet.

    Mode (sandbox vs live) is fixed by the deployment's AgentCard credential; there is no per-item test flag. user_id may only reference a user already enrolled by a wallet in this organization.
    """

    provider: Required[Literal["agentcard"]]

    user_id: str


WalletVaultItemSpecParam: TypeAlias = Union[LinkWalletVaultItemSpec, AgentCardWalletVaultItemSpec]
