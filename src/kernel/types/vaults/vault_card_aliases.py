# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["VaultCardAliases"]


class VaultCardAliases(BaseModel):
    cvc: str

    exp_month: str

    exp_year: str

    number: str
