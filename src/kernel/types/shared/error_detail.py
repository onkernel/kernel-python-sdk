# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ErrorDetail"]


class ErrorDetail(BaseModel):
    code: Optional[str] = None
    """Lower-level error code providing more specific detail"""

    message: Optional[str] = None
    """Further detail about the error"""
