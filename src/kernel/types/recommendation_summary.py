# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .recommendation import Recommendation

__all__ = ["RecommendationSummary"]


class RecommendationSummary(BaseModel):
    last_requested_at: datetime
    """Most recent time the selected project requested an analysis for this domain."""

    recommendation: Optional[Recommendation] = None
    """Current domain-level recommendation. Null when no eligible knowledge exists."""

    recommended_config_label: Optional[str] = None
    """Display label for the recommended browser configuration."""

    success_rate: Optional[float] = None
    """Success rate for the recommended configuration.

    Null when no eligible knowledge exists.
    """

    target: str
    """Registrable domain previously analyzed by the selected project."""
