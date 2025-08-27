# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["FUploadParams", "File"]


class FUploadParams(TypedDict, total=False):
    files: Required[Iterable[File]]


class File(TypedDict, total=False):
    dest_path: Required[str]
    """Absolute destination path to write the file."""

    file: Required[FileTypes]
