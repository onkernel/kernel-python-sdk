# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .discovered_field import DiscoveredField

__all__ = ["AgentAuthSubmitResponse"]


class AgentAuthSubmitResponse(BaseModel):
    """Response from submit endpoint matching SubmitResult schema"""

    success: bool
    """Whether submission succeeded"""

    additional_fields: Optional[List[DiscoveredField]] = None
    """
    Additional fields needed (e.g., OTP) - present when needs_additional_auth is
    true
    """

    app_name: Optional[str] = None
    """App name (only present when logged_in is true)"""

    error_message: Optional[str] = None
    """Error message if submission failed"""

    logged_in: Optional[bool] = None
    """Whether user is now logged in"""

    needs_additional_auth: Optional[bool] = None
    """Whether additional authentication fields are needed"""

    target_domain: Optional[str] = None
    """Target domain (only present when logged_in is true)"""
