# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SiteConfigResolveParams"]


class SiteConfigResolveParams(TypedDict, total=False):
    url: Required[str]
    """Public HTTP(S) URL to refresh."""

    allowed_proxy_countries: SequenceNotStr[str]
    """
    ISO 3166 country codes Kernel may use when searching for or returning a proxy
    configuration. Kernel may test a subset of allowed countries. When omitted,
    Kernel uses its default country selection.
    """
