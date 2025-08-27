# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProcessSpawnParams"]


class ProcessSpawnParams(TypedDict, total=False):
    command: Required[str]
    """Executable or shell command to run."""

    args: List[str]
    """Command arguments."""

    as_root: bool
    """Run the process with root privileges."""

    as_user: Optional[str]
    """Run the process as this user."""

    cwd: Optional[str]
    """Working directory (absolute path) to run the command in."""

    env: Dict[str, str]
    """Environment variables to set for the process."""

    timeout_sec: Optional[int]
    """Maximum execution time in seconds."""
