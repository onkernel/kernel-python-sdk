# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtensionDownloadFromChromeStoreParams"]


class ExtensionDownloadFromChromeStoreParams(TypedDict, total=False):
    url: Required[str]
    """Chrome Web Store URL for the extension."""

    os: Literal["win", "mac", "linux"]
    """Target operating system for the extension package. Defaults to linux."""
