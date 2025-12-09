# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InvocationExchangeResponse"]


class InvocationExchangeResponse(BaseModel):
    """Response from exchange endpoint"""

    invocation_id: str
    """Invocation ID"""

    jwt: str
    """JWT token with invocation_id claim (30 minute TTL)"""
