# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProcessStdinParams"]


class ProcessStdinParams(TypedDict, total=False):
    id: Required[str]

    data_b64: Required[str]
    """Base64-encoded data to write."""
