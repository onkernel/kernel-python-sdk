# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .tool_source import ToolSource
from .tool_annotations import ToolAnnotations

__all__ = ["Tool"]


class Tool(BaseModel):
    description: str

    input_schema: Dict[str, object]

    name: str

    source: ToolSource

    tool_ref: str
    """Opaque reference for invoking this exact live registration.

    It becomes invalid when its document or browser process is replaced.
    """

    annotations: Optional[ToolAnnotations] = None
    """Page-provided behavioral hints.

    These values are untrusted and are not enforced by Kernel.
    """
