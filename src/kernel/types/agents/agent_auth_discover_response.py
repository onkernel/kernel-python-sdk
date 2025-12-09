# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .discovered_field import DiscoveredField

__all__ = ["AgentAuthDiscoverResponse"]


class AgentAuthDiscoverResponse(BaseModel):
    """Response from discover endpoint matching AuthBlueprint schema"""

    success: bool
    """Whether discovery succeeded"""

    error_message: Optional[str] = None
    """Error message if discovery failed"""

    fields: Optional[List[DiscoveredField]] = None
    """Discovered form fields (present when success is true)"""

    logged_in: Optional[bool] = None
    """Whether user is already logged in"""

    login_url: Optional[str] = None
    """URL of the discovered login page"""

    page_title: Optional[str] = None
    """Title of the login page"""
