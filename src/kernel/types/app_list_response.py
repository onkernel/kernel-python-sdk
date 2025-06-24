# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["AppListResponse", "AppListResponseItem"]


class AppListResponseItem(BaseModel):
    id: str
    """Unique identifier for the app version"""

    app_name: str
    """Name of the application"""

    deployment: str
    """Deployment ID"""

    region: Literal["aws.us-east-1a"]
    """Deployment region code"""

    version: str
    """Version label for the application"""

    env_vars: Optional[Dict[str, str]] = None
    """Environment variables configured for this app version"""


AppListResponse: TypeAlias = List[AppListResponseItem]
