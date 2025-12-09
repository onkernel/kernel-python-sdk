# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProcessExecResponse"]


class ProcessExecResponse(BaseModel):
    """Result of a synchronous command execution."""

    duration_ms: Optional[int] = None
    """Execution duration in milliseconds."""

    exit_code: Optional[int] = None
    """Process exit code."""

    stderr_b64: Optional[str] = None
    """Base64-encoded stderr buffer."""

    stdout_b64: Optional[str] = None
    """Base64-encoded stdout buffer."""
