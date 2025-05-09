# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppInvokeParams"]


class AppInvokeParams(TypedDict, total=False):
    action_name: Required[Annotated[str, PropertyInfo(alias="actionName")]]
    """Name of the action to invoke"""

    app_name: Required[Annotated[str, PropertyInfo(alias="appName")]]
    """Name of the application"""

    payload: Required[object]
    """Input data for the application"""

    version: Required[str]
    """Version of the application"""
