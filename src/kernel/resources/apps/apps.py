# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .deployments import (
    DeploymentsResource,
    AsyncDeploymentsResource,
    DeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
)
from .invocations import (
    InvocationsResource,
    AsyncInvocationsResource,
    InvocationsResourceWithRawResponse,
    AsyncInvocationsResourceWithRawResponse,
    InvocationsResourceWithStreamingResponse,
    AsyncInvocationsResourceWithStreamingResponse,
)

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def deployments(self) -> DeploymentsResource:
        return DeploymentsResource(self._client)

    @cached_property
    def invocations(self) -> InvocationsResource:
        return InvocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def invocations(self) -> AsyncInvocationsResource:
        return AsyncInvocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self._apps.deployments)

    @cached_property
    def invocations(self) -> InvocationsResourceWithRawResponse:
        return InvocationsResourceWithRawResponse(self._apps.invocations)


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self._apps.deployments)

    @cached_property
    def invocations(self) -> AsyncInvocationsResourceWithRawResponse:
        return AsyncInvocationsResourceWithRawResponse(self._apps.invocations)


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self._apps.deployments)

    @cached_property
    def invocations(self) -> InvocationsResourceWithStreamingResponse:
        return InvocationsResourceWithStreamingResponse(self._apps.invocations)


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self._apps.deployments)

    @cached_property
    def invocations(self) -> AsyncInvocationsResourceWithStreamingResponse:
        return AsyncInvocationsResourceWithStreamingResponse(self._apps.invocations)
