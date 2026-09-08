# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .vault_item_event import VaultItemEvent

__all__ = ["ItemEventsResponse"]

ItemEventsResponse: TypeAlias = List[VaultItemEvent]
