# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["RunExchangeResponse"]


class RunExchangeResponse(BaseModel):
    jwt: str
    """JWT token with run_id claim (30 minute TTL)"""

    run_id: str
    """Run ID"""
