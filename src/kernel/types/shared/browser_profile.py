# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserProfile"]


class BrowserProfile(BaseModel):
    """Profile selection for the browser session.

    Provide either id or name. If specified, the
    matching profile will be loaded into the browser session. Profiles must be created beforehand.
    """

    id: Optional[str] = None
    """Profile ID to load for this browser session"""

    name: Optional[str] = None
    """Profile name to load for this browser session (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
    """

    save_changes: Optional[bool] = None
    """
    If true, save changes made during the session back to the profile when the
    session ends.
    """
