# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ToolFrame"]


class ToolFrame(BaseModel):
    frame_id: int
    """
    Monotonically increasing identifier for this embedded frame during the current
    browser process.
    """

    url: str
    """Current frame URL with the fragment omitted."""
