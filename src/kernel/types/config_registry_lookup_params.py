# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ConfigRegistryLookupParams"]


class ConfigRegistryLookupParams(TypedDict, total=False):
    url: Required[str]
    """Public HTTP(S) URL to look up."""

    allowed_proxy_countries: SequenceNotStr[str]
    """ISO 3166 country codes Kernel may use when returning a proxy configuration.

    When omitted, Kernel uses its default country selection.
    """
