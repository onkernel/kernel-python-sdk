# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["AppDeployParams"]


class AppDeployParams(TypedDict, total=False):
    app_name: Required[Annotated[str, PropertyInfo(alias="appName")]]
    """Name of the application"""

    file: Required[FileTypes]
    """ZIP file containing the application"""

    version: Required[str]
    """Version of the application"""

    region: str
    """AWS region for deployment (e.g. "aws.us-east-1a")"""
