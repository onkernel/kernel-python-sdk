# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserProfile"]


class BrowserProfile(TypedDict, total=False):
    """Profile selection for the browser session.

    Provide either id or name. If specified, the
    matching profile will be loaded into the browser session. Profiles must be created beforehand.
    """

    id: str
    """Profile ID to load for this browser session"""

    name: str
    """Profile name to load for this browser session (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
    """

    save_changes: bool
    """
    If true, save changes made during the session back to the profile when the
    session ends.
    """
