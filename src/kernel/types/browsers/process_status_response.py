# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProcessStatusResponse"]


class ProcessStatusResponse(BaseModel):
    """Current status of a process."""

    cpu_pct: Optional[float] = None
    """Estimated CPU usage percentage."""

    exit_code: Optional[int] = None
    """Exit code if the process has exited."""

    mem_bytes: Optional[int] = None
    """Estimated resident memory usage in bytes."""

    state: Optional[Literal["running", "exited"]] = None
    """Process state."""
