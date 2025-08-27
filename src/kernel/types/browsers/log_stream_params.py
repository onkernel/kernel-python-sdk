# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LogStreamParams"]


class LogStreamParams(TypedDict, total=False):
    source: Required[Literal["path", "supervisor"]]

    follow: bool

    path: str
    """only required if source is path"""

    supervisor_process: str
    """only required if source is supervisor"""
