# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AppDeployResponse", "App", "AppAction"]


class AppAction(BaseModel):
    name: str
    """Name of the action"""


class App(BaseModel):
    id: str
    """ID for the app version deployed"""

    actions: List[AppAction]

    name: str
    """Name of the app"""


class AppDeployResponse(BaseModel):
    apps: List[App]

    message: str
    """Success message"""

    success: bool
    """Status of the deployment"""
