# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserExtension"]


class BrowserExtension(BaseModel):
    """Extension selection for the browser session.

    Provide either id or name of an extension uploaded to Kernel.
    """

    id: Optional[str] = None
    """Extension ID to load for this browser session"""

    name: Optional[str] = None
    """Extension name to load for this browser session (instead of id).

    Must be 1-255 characters, using letters, numbers, dots, underscores, or hyphens.
    """
