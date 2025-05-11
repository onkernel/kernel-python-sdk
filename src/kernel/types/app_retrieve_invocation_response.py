# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppRetrieveInvocationResponse"]


class AppRetrieveInvocationResponse(BaseModel):
    id: str

    app_name: str = FieldInfo(alias="appName")

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    input: str

    output: str

    started_at: str = FieldInfo(alias="startedAt")

    status: str
