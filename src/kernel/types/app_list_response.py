# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.app_action import AppAction

__all__ = ["AppListResponse", "AppListResponseItem"]


class AppListResponseItem(BaseModel):
    id: str
    """Unique identifier for the app version"""

    actions: List[AppAction]
    """List of actions available on the app"""

    app_name: str
    """Name of the application"""

    deployment: str
    """Deployment ID"""

    env_vars: Dict[str, str]
    """Environment variables configured for this app version"""

    region: Literal["aws.us-east-1a"]
    """Deployment region code"""

    version: str
    """Version label for the application"""


AppListResponse: TypeAlias = List[AppListResponseItem]
