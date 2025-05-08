# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AppInvokeResponse"]


class AppInvokeResponse(BaseModel):
    id: str
    """ID of the invocation"""

    status: str
    """Status of the invocation"""
