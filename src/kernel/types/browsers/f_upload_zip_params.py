# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["FUploadZipParams"]


class FUploadZipParams(TypedDict, total=False):
    dest_path: Required[str]
    """Absolute destination directory to extract the archive to."""

    zip_file: Required[FileTypes]
