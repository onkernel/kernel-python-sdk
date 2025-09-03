# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ProcessExecParams"]


class ProcessExecParams(TypedDict, total=False):
    command: Required[str]
    """Executable or shell command to run."""

    args: SequenceNotStr[str]
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
