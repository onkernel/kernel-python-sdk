# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .shared.log_event import LogEvent
from .shared.error_event import ErrorEvent
from .invocation_state_event import InvocationStateEvent

__all__ = ["InvocationFollowResponse"]

InvocationFollowResponse: TypeAlias = Annotated[
    Union[LogEvent, InvocationStateEvent, ErrorEvent], PropertyInfo(discriminator="event")
]
