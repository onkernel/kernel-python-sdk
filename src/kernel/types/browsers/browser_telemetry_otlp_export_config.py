# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserTelemetryOtlpExportConfig"]


class BrowserTelemetryOtlpExportConfig(BaseModel):
    """Active OTLP export state for a browser session."""

    destination: Optional[str] = None
    """ID of the OTLP destination the session is bound to.

    Omitted when the session is not exporting.
    """

    enabled: Optional[bool] = None
    """Whether the session is exporting captured telemetry over OTLP."""
