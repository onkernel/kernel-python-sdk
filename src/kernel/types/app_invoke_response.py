# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AppInvokeResponse"]


class AppInvokeResponse(BaseModel):
    id: str
    """ID of the invocation"""

    status: Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED"]
    """Status of the invocation"""

    output: Optional[str] = None
    """Output from the invocation (if available)"""
