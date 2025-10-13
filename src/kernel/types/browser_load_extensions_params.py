# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["BrowserLoadExtensionsParams", "Extension"]


class BrowserLoadExtensionsParams(TypedDict, total=False):
    extensions: Required[Iterable[Extension]]
    """List of extensions to upload and activate"""


class Extension(TypedDict, total=False):
    name: Required[str]
    """Folder name to place the extension under /home/kernel/extensions/<name>"""

    zip_file: Required[FileTypes]
    """
    Zip archive containing an unpacked Chromium extension (must include
    manifest.json)
    """
