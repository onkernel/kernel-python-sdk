# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuditLogExportDestination"]


class AuditLogExportDestination(BaseModel):
    """An organization-scoped audit log export destination.

    Delivery is at-least-once for rows visible when their window is committed: a delivery that is retried rewrites the same object, and the same `event_id` can appear in more than one object, so consumers must deduplicate on `event_id`. Each event-time window is held for ten minutes before it commits; a row that becomes visible after its window is committed may not be delivered.

    Objects are written as `<prefix>/destination_id=<destination>/org_id=<org>/date=<YYYY-MM-DD>/hour=<HH>/<window>-<chunk>.jsonl.gz`, where `date` and `hour` are the UTC calendar hour that fully contains every row in the object, so the layout is safe to register as a Hive-partitioned table. The object name is derived from the rows it holds, so a retried delivery rewrites its own object.
    """

    id: str

    bucket: str

    consecutive_failures: int

    created_at: datetime

    external_id: str

    format: Literal["jsonl.gz"]

    kernel_role_arn: str
    """The Kernel role that assumes `role_arn` in your account to deliver logs.

    Allow this role as the principal in your role's trust policy, and require
    `external_id` as the `sts:ExternalId` condition.

    Recreating a destination issues a new `external_id`, which the trust policy has
    to be updated to match.
    """

    prefix: str

    region: str

    role_arn: str

    status: Literal["active", "paused"]
    """Pausing prevents new delivery attempts.

    An S3 upload already in progress may complete after the pause response; its rows
    can appear again after the destination is resumed.
    """

    type: Literal["s3"]

    updated_at: datetime

    kms_key_id: Optional[str] = None

    last_error: Optional[str] = None
    """Sanitized description of the most recent delivery failure."""

    last_error_at: Optional[datetime] = None

    last_exported_cursor: Optional[str] = None
    """Opaque, versioned checkpoint for forward-only continuous export.

    This value is not compatible with audit-log list page tokens.

    Delivery starts at the moment the destination is activated, so events recorded
    before that are not delivered. Pausing stops delivery and resuming starts again
    from the time of the resume: events recorded while a destination was paused are
    never exported, and pausing is not a way to defer delivery.
    """

    last_success_at: Optional[datetime] = None

    next_attempt_at: Optional[datetime] = None
