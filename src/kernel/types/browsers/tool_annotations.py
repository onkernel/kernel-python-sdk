# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ToolAnnotations"]


class ToolAnnotations(BaseModel):
    """Page-provided behavioral hints.

    These values are untrusted and are not enforced by Kernel.
    """

    autosubmit: bool

    consequential: bool

    read_only: bool

    untrusted_content: bool
