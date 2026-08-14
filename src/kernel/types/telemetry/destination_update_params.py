# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["DestinationUpdateParams"]


class DestinationUpdateParams(TypedDict, total=False):
    description: str

    endpoint: str
    """Base endpoint of the OTLP/HTTP collector, without a signal path.

    Same rules as on create.
    """

    headers: Dict[str, Optional[str]]
    """Edits stored headers key by key rather than replacing the map.

    A string value adds or replaces that header, `null` deletes it, and any key you
    omit is left as it is. Names are matched case-insensitively, so `authorization`
    replaces a stored `Authorization` rather than adding a second entry. This is the
    credential rotation path; sessions already exporting pick up the new values
    without restarting. Names and values must be valid HTTP header tokens, and the
    names and values together cannot exceed 8192 bytes.
    """

    name: str
