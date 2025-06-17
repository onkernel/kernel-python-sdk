# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvocationCreateParams"]


class InvocationCreateParams(TypedDict, total=False):
    action_name: Required[str]
    """Name of the action to invoke"""

    app_name: Required[str]
    """Name of the application"""

    version: Required[str]
    """Version of the application"""

    async_: Annotated[bool, PropertyInfo(alias="async")]
    """If true, invoke asynchronously.

    When set, the API responds 202 Accepted with status "queued".
    """

    payload: str
    """Input data for the action, sent as a JSON string."""
