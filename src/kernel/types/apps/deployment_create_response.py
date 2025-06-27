# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.app_action import AppAction

__all__ = ["DeploymentCreateResponse", "App"]


class App(BaseModel):
    id: str
    """ID for the app version deployed"""

    actions: List[AppAction]
    """List of actions available on the app"""

    name: str
    """Name of the app"""


class DeploymentCreateResponse(BaseModel):
    apps: List[App]
    """List of apps deployed"""

    status: Literal["queued", "deploying", "succeeded", "failed"]
    """Current status of the deployment"""

    status_reason: Optional[str] = None
    """Status reason"""
