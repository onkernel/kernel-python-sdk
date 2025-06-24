# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeploymentFollowParams"]


class DeploymentFollowParams(TypedDict, total=False):
    since: str
    """Show logs since the given time (RFC timestamps or durations like 5m)."""
