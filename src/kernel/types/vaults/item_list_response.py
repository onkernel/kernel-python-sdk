# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .vault_item import VaultItem

__all__ = ["ItemListResponse"]

ItemListResponse: TypeAlias = List[VaultItem]
