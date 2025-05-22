# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BrowserPersistence"]


class BrowserPersistence(BaseModel):
    id: str
    """Unique identifier for the persistent browser session."""
