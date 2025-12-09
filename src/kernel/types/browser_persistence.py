# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BrowserPersistence"]


class BrowserPersistence(BaseModel):
    """DEPRECATED: Use timeout_seconds (up to 72 hours) and Profiles instead."""

    id: str
    """DEPRECATED: Unique identifier for the persistent browser session."""
