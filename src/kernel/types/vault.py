# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Vault"]


class Vault(BaseModel):
    id: str

    created_at: datetime

    name: str
    """Immutable name assigned when the vault is created."""

    updated_at: datetime
