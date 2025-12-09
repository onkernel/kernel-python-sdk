# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProcessStdoutStreamResponse"]


class ProcessStdoutStreamResponse(BaseModel):
    """SSE payload representing process output or lifecycle events."""

    data_b64: Optional[str] = None
    """Base64-encoded data from the process stream."""

    event: Optional[Literal["exit"]] = None
    """Lifecycle event type."""

    exit_code: Optional[int] = None
    """Exit code when the event is "exit"."""

    stream: Optional[Literal["stdout", "stderr"]] = None
    """Source stream of the data chunk."""
