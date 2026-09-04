# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "WalletVaultItemSpec",
    "LinkWalletVaultItemSpec",
    "LinkWalletVaultItemSpecAuthorization",
    "LinkWalletVaultItemSpecAuthorizationClient",
    "AgentCardWalletVaultItemSpec",
]


class LinkWalletVaultItemSpecAuthorizationClient(BaseModel):
    type: Literal["kernel_managed"]


class LinkWalletVaultItemSpecAuthorization(BaseModel):
    client: LinkWalletVaultItemSpecAuthorizationClient

    method: Literal["oauth"]


class LinkWalletVaultItemSpec(BaseModel):
    authorization: LinkWalletVaultItemSpecAuthorization

    provider: Literal["link"]


class AgentCardWalletVaultItemSpec(BaseModel):
    """AgentCard wallet.

    Mode (sandbox vs live) is fixed by the deployment's AgentCard credential; there is no per-item test flag. user_id may only reference a user already enrolled by a wallet in this organization.
    """

    provider: Literal["agentcard"]

    user_id: Optional[str] = None


WalletVaultItemSpec: TypeAlias = Annotated[
    Union[LinkWalletVaultItemSpec, AgentCardWalletVaultItemSpec], PropertyInfo(discriminator="provider")
]
