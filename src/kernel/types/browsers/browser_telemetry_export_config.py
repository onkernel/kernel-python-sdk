# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .browser_telemetry_otlp_export_config import BrowserTelemetryOtlpExportConfig

__all__ = ["BrowserTelemetryExportConfig"]


class BrowserTelemetryExportConfig(BaseModel):
    """Active export state for a session's captured telemetry, by protocol."""

    otlp: Optional[BrowserTelemetryOtlpExportConfig] = None
    """Active OTLP export state."""
