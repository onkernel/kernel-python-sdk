# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import browser_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.browser_create_response import BrowserCreateResponse
from ..types.browser_retrieve_response import BrowserRetrieveResponse

__all__ = ["BrowsersResource", "AsyncBrowsersResource"]


class BrowsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrowsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return BrowsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        invocation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserCreateResponse:
        """
        Create Browser Session

        Args:
          invocation_id: action invocation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/browsers",
            body=maybe_transform({"invocation_id": invocation_id}, browser_create_params.BrowserCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserRetrieveResponse:
        """
        Get Browser Session by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserRetrieveResponse,
        )


class AsyncBrowsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncBrowsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        invocation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserCreateResponse:
        """
        Create Browser Session

        Args:
          invocation_id: action invocation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/browsers",
            body=await async_maybe_transform(
                {"invocation_id": invocation_id}, browser_create_params.BrowserCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserRetrieveResponse:
        """
        Get Browser Session by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserRetrieveResponse,
        )


class BrowsersResourceWithRawResponse:
    def __init__(self, browsers: BrowsersResource) -> None:
        self._browsers = browsers

        self.create = to_raw_response_wrapper(
            browsers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            browsers.retrieve,
        )


class AsyncBrowsersResourceWithRawResponse:
    def __init__(self, browsers: AsyncBrowsersResource) -> None:
        self._browsers = browsers

        self.create = async_to_raw_response_wrapper(
            browsers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            browsers.retrieve,
        )


class BrowsersResourceWithStreamingResponse:
    def __init__(self, browsers: BrowsersResource) -> None:
        self._browsers = browsers

        self.create = to_streamed_response_wrapper(
            browsers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            browsers.retrieve,
        )


class AsyncBrowsersResourceWithStreamingResponse:
    def __init__(self, browsers: AsyncBrowsersResource) -> None:
        self._browsers = browsers

        self.create = async_to_streamed_response_wrapper(
            browsers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            browsers.retrieve,
        )
