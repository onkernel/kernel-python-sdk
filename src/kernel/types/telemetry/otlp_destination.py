# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["OtlpDestination"]


class OtlpDestination(BaseModel):
    """An OTLP endpoint to export browser session telemetry to.

    Reference one from `telemetry.export.otlp.destination` when creating a browser to export that session's captured telemetry to it.
    """

    id: str

    created_at: datetime

    endpoint: str
    """OTLP/HTTP endpoint telemetry is sent to."""

    headers: Dict[str, str]
    """Headers sent with each export request.

    Names are returned in canonical form (`Authorization`, not `authorization`).
    Non-dashboard reads return values redacted as empty strings, so the keys are
    visible but the credentials are not. Dashboard reads return the stored values.
    """

    name: str
    """Unique within the organization.

    Usable in place of the ID when selecting a destination, so it cannot be shaped
    like an ID.
    """

    updated_at: datetime

    description: Optional[str] = None
