# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["CredentialUpdateParams"]


class CredentialUpdateParams(TypedDict, total=False):
    name: str
    """New name for the credential"""

    values: Dict[str, str]
    """Field name to value mapping (e.g., username, password).

    Replaces all existing values.
    """
