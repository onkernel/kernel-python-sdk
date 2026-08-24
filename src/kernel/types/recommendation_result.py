# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .recommendation import Recommendation
from .no_recommendation import NoRecommendation

__all__ = ["RecommendationResult"]

RecommendationResult: TypeAlias = Annotated[Union[Recommendation, NoRecommendation], PropertyInfo(discriminator="type")]
