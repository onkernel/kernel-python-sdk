# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    domain: Required[str]
    """Target domain this credential is for"""

    name: Required[str]
    """Unique name for the credential within the organization"""

    values: Required[Dict[str, str]]
    """Field name to value mapping (e.g., username, password)"""
