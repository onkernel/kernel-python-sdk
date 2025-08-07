# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["FFileInfoResponse"]


class FFileInfoResponse(BaseModel):
    is_dir: bool
    """Whether the path is a directory."""

    mod_time: datetime
    """Last modification time."""

    mode: str
    """File mode bits (e.g., "drwxr-xr-x" or "-rw-r--r--")."""

    name: str
    """Base name of the file or directory."""

    path: str
    """Absolute path."""

    size_bytes: int
    """Size in bytes. 0 for directories."""
