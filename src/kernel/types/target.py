# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Target"]


class Target(BaseModel):
    domain: str
    """Registrable domain."""

    host: str
    """Full hostname, including subdomain."""

    normalized: str
    """Exact normalized scheme, host, port, and path used for lookup."""
