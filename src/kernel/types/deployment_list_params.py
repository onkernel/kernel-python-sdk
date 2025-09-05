# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    app_name: Required[str]
    """Filter results by application name."""

    limit: int
    """Limit the number of deployments to return."""

    offset: int
    """Offset the number of deployments to return."""
