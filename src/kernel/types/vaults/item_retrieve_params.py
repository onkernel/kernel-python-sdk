# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemRetrieveParams"]


class ItemRetrieveParams(TypedDict, total=False):
    id_or_name: Required[str]

    expand: List[Literal["payment_methods"]]
    """Live fields advertised by `available_expansions` to include in `expanded`."""

    wait: int
    """
    Hold for up to this many seconds while the item is pending authorization or
    approval.
    """
