# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Credential"]


class Credential(BaseModel):
    """A stored credential for automatic re-authentication"""

    id: str
    """Unique identifier for the credential"""

    created_at: datetime
    """When the credential was created"""

    domain: str
    """Target domain this credential is for"""

    name: str
    """Unique name for the credential within the organization"""

    updated_at: datetime
    """When the credential was last updated"""
