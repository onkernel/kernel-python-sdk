# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuthAgent"]


class AuthAgent(BaseModel):
    """
    An auth agent that manages authentication for a specific domain and profile combination
    """

    id: str
    """Unique identifier for the auth agent"""

    domain: str
    """Target domain for authentication"""

    profile_name: str
    """Name of the profile associated with this auth agent"""

    status: Literal["AUTHENTICATED", "NEEDS_AUTH"]
    """Current authentication status of the managed profile"""

    last_auth_check_at: Optional[datetime] = None
    """When the last authentication check was performed"""
