# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExportDestinationCreateParams"]


class ExportDestinationCreateParams(TypedDict, total=False):
    bucket: Required[str]

    format: Required[Literal["jsonl.gz"]]

    prefix: Required[str]

    region: Required[str]

    role_arn: Required[str]

    type: Required[Literal["s3"]]

    kms_key_id: str
