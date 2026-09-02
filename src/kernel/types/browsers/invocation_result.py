# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InvocationResult"]


class InvocationResult(BaseModel):
    invocation_id: str

    status: Literal["completed", "canceled", "error"]

    error_text: Optional[str] = None

    output: Optional[object] = None
    """Untrusted page-provided output.

    Callers must treat it as potentially malicious input.
    """
