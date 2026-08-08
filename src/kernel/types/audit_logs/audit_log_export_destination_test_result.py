# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuditLogExportDestinationTestResult", "Error"]


class Error(BaseModel):
    code: Literal["assume_role_failed", "put_object_failed"]

    message: str


class AuditLogExportDestinationTestResult(BaseModel):
    stage: Literal["assume_role", "put_object", "complete"]

    success: bool

    error: Optional[Error] = None
