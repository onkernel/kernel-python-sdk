# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AppAction"]


class AppAction(BaseModel):
    """An action available on the app"""

    name: str
    """Name of the action"""
