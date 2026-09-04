# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VaultReference"]


class VaultReference(BaseModel):
    """Reference to a project-scoped vault. Provide exactly one of id or name."""

    id: Optional[str] = None

    name: Optional[str] = None
