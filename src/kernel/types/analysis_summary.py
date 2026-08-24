# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .target import Target
from .._models import BaseModel
from .analysis import Analysis

__all__ = ["AnalysisSummary"]


class AnalysisSummary(BaseModel):
    analysis: Analysis

    target: Target
