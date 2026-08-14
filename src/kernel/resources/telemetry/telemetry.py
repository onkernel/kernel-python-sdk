# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .destinations import (
    DestinationsResource,
    AsyncDestinationsResource,
    DestinationsResourceWithRawResponse,
    AsyncDestinationsResourceWithRawResponse,
    DestinationsResourceWithStreamingResponse,
    AsyncDestinationsResourceWithStreamingResponse,
)

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    @cached_property
    def destinations(self) -> DestinationsResource:
        """
        Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
        """
        return DestinationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return TelemetryResourceWithStreamingResponse(self)


class AsyncTelemetryResource(AsyncAPIResource):
    @cached_property
    def destinations(self) -> AsyncDestinationsResource:
        """
        Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
        """
        return AsyncDestinationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncTelemetryResourceWithStreamingResponse(self)


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def destinations(self) -> DestinationsResourceWithRawResponse:
        """
        Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
        """
        return DestinationsResourceWithRawResponse(self._telemetry.destinations)


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def destinations(self) -> AsyncDestinationsResourceWithRawResponse:
        """
        Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
        """
        return AsyncDestinationsResourceWithRawResponse(self._telemetry.destinations)


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def destinations(self) -> DestinationsResourceWithStreamingResponse:
        """
        Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
        """
        return DestinationsResourceWithStreamingResponse(self._telemetry.destinations)


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

    @cached_property
    def destinations(self) -> AsyncDestinationsResourceWithStreamingResponse:
        """
        Stream live telemetry events from a browser session, and manage the destinations sessions export them to.
        """
        return AsyncDestinationsResourceWithStreamingResponse(self._telemetry.destinations)
