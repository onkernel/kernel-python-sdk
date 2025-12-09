# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WatchEventsResponse"]


class WatchEventsResponse(BaseModel):
    """Filesystem change event."""

    path: str
    """Absolute path of the file or directory."""

    type: Literal["CREATE", "WRITE", "DELETE", "RENAME"]
    """Event type."""

    is_dir: Optional[bool] = None
    """Whether the affected path is a directory."""

    name: Optional[str] = None
    """Base name of the file or directory affected."""
