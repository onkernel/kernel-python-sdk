# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .proxy import Proxy
from .browser import Browser
from .._models import BaseModel
from .evidence import Evidence

__all__ = ["Recommendation"]


class Recommendation(BaseModel):
    browser: Browser
    """Browser settings that can be passed directly to `POST /browsers`."""

    evidence: Evidence

    match_scope: Literal["exact", "host", "domain"]
    """Specificity of knowledge matched for this recommendation."""

    matched_target: str
    """Target value that supplied the recommendation."""

    proxy: Proxy
    """Proxy recipe for the recommended browser."""

    type: Literal["recommendation"]

    verification: Literal["verified", "inferred"]
    """
    Exact matches meet the evidence threshold; host and domain fallbacks are
    inferred. Check evidence.last_verified_at for successful verification age and
    last_observed_at for the latest evidence.
    """
