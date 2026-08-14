# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["DestinationCreateParams"]


class DestinationCreateParams(TypedDict, total=False):
    endpoint: Required[str]
    """Base endpoint of the OTLP/HTTP collector, without a signal path.

    Kernel appends the signal path itself, so pass `https://api.honeycomb.io` rather
    than `https://api.honeycomb.io/v1/logs`. If your provider's docs give you a
    signal-specific URL, drop the trailing `/v1/logs`, `/v1/traces`, or
    `/v1/metrics` — an endpoint that already carries one is rejected.

    Must be http or https, must resolve to a public address, and must carry no query
    string or fragment. Examples: `https://api.honeycomb.io`,
    `https://otlp-gateway-prod-us-east-0.grafana.net/otlp`,
    `https://otlp.datadoghq.com` (Datadog's OTLP intake for US1, not its logs
    intake).
    """

    name: Required[str]
    """Unique within the project."""

    description: str

    headers: Dict[str, str]
    """Headers sent with each export request, typically an ingestion key.

    Encrypted at rest and returned redacted. Names and values must be valid HTTP
    header tokens, and the names and values together cannot exceed 8192 bytes. Names
    are matched case-insensitively and stored canonicalized, so supplying two
    spellings of one header is rejected.
    """
