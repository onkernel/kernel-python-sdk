# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AppDeployResponse"]


class AppDeployResponse(BaseModel):
    id: str
    """ID of the deployed app version"""

    message: str
    """Success message"""

    success: bool
    """Status of the deployment"""
