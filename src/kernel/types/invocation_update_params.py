# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InvocationUpdateParams"]


class InvocationUpdateParams(TypedDict, total=False):
    status: Required[Literal["succeeded", "failed"]]
    """New status for the invocation."""

    output: str
    """Updated output of the invocation rendered as JSON string."""
