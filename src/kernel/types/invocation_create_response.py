# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvocationCreateResponse"]


class InvocationCreateResponse(BaseModel):
    id: str
    """ID of the invocation"""

    action_name: str
    """Name of the action invoked"""

    status: Literal["queued", "running", "succeeded", "failed"]
    """Status of the invocation"""

    output: Optional[str] = None
    """The return value of the action that was invoked, rendered as a JSON string.

    This could be: string, number, boolean, array, object, or null.
    """

    status_reason: Optional[str] = None
    """Status reason"""
