# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProcessStdinResponse"]


class ProcessStdinResponse(BaseModel):
    """Result of writing to stdin."""

    written_bytes: Optional[int] = None
    """Number of bytes written."""
