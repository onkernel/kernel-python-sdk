# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["AppDeployParams"]


class AppDeployParams(TypedDict, total=False):
    entrypoint_rel_path: Required[Annotated[str, PropertyInfo(alias="entrypointRelPath")]]
    """Relative path to the entrypoint of the application"""

    file: Required[FileTypes]
    """ZIP file containing the application source directory"""

    force: Literal["true", "false"]
    """Allow overwriting an existing app version"""

    region: Literal["aws.us-east-1a"]
    """Region for deployment. Currently we only support "aws.us-east-1a" """

    version: str
    """Version of the application. Can be any string."""
