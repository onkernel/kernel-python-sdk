# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProcessKillParams"]


class ProcessKillParams(TypedDict, total=False):
    id: Required[str]

    signal: Required[Literal["TERM", "KILL", "INT", "HUP"]]
    """Signal to send."""
