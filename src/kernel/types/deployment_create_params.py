# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    entrypoint_rel_path: Required[str]
    """Relative path to the entrypoint of the application"""

    file: Required[FileTypes]
    """ZIP file containing the application source directory"""

    env_vars: Dict[str, str]
    """Map of environment variables to set for the deployed application.

    Each key-value pair represents an environment variable.
    """

    force: bool
    """Allow overwriting an existing app version"""

    region: Literal["aws.us-east-1a"]
    """Region for deployment. Currently we only support "aws.us-east-1a" """

    version: str
    """Version of the application. Can be any string."""
