# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrowserPoolAcquireParams"]


class BrowserPoolAcquireParams(TypedDict, total=False):
    acquire_timeout_seconds: int
    """Maximum number of seconds to wait for a browser to be available.

    Defaults to the calculated time it would take to fill the pool at the currently
    configured fill rate.
    """
