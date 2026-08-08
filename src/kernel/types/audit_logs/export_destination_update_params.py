# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExportDestinationUpdateParams"]


class ExportDestinationUpdateParams(TypedDict, total=False):
    bucket: str

    kms_key_id: str
    """KMS key ID, alias, or ARN.

    Set to an empty string to remove the configured KMS key; omit or send null to
    leave unchanged.
    """

    prefix: str

    region: str

    role_arn: str

    status: Literal["active", "paused"]
