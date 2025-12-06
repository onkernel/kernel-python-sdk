# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["InvocationSubmitParams"]


class InvocationSubmitParams(TypedDict, total=False):
    field_values: Required[Dict[str, str]]
    """Values for the discovered login fields"""
