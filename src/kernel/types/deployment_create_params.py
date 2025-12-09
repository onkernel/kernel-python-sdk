# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["DeploymentCreateParams", "Source", "SourceAuth"]


class DeploymentCreateParams(TypedDict, total=False):
    entrypoint_rel_path: str
    """Relative path to the entrypoint of the application"""

    env_vars: Dict[str, str]
    """Map of environment variables to set for the deployed application.

    Each key-value pair represents an environment variable.
    """

    file: FileTypes
    """ZIP file containing the application source directory"""

    force: bool
    """Allow overwriting an existing app version"""

    region: Literal["aws.us-east-1a"]
    """Region for deployment. Currently we only support "aws.us-east-1a" """

    source: Source
    """Source from which to fetch application code."""

    version: str
    """Version of the application. Can be any string."""


class SourceAuth(TypedDict, total=False):
    """Authentication for private repositories."""

    token: Required[str]
    """GitHub PAT or installation access token"""

    method: Required[Literal["github_token"]]
    """Auth method"""


class Source(TypedDict, total=False):
    """Source from which to fetch application code."""

    entrypoint: Required[str]
    """Relative path to the application entrypoint within the selected path."""

    ref: Required[str]
    """Git ref (branch, tag, or commit SHA) to fetch."""

    type: Required[Literal["github"]]
    """Source type identifier."""

    url: Required[str]
    """Base repository URL (without blob/tree suffixes)."""

    auth: SourceAuth
    """Authentication for private repositories."""

    path: str
    """Path within the repo to deploy (omit to use repo root)."""
