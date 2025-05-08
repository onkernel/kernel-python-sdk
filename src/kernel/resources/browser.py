# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.browser_create_session_response import BrowserCreateSessionResponse

__all__ = ["BrowserResource", "AsyncBrowserResource"]


class BrowserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return BrowserResourceWithStreamingResponse(self)

    def create_session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserCreateSessionResponse:
        """Create Browser Session"""
        return self._post(
            "/browser",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserCreateSessionResponse,
        )


class AsyncBrowserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncBrowserResourceWithStreamingResponse(self)

    async def create_session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserCreateSessionResponse:
        """Create Browser Session"""
        return await self._post(
            "/browser",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserCreateSessionResponse,
        )


class BrowserResourceWithRawResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

        self.create_session = to_raw_response_wrapper(
            browser.create_session,
        )


class AsyncBrowserResourceWithRawResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

        self.create_session = async_to_raw_response_wrapper(
            browser.create_session,
        )


class BrowserResourceWithStreamingResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

        self.create_session = to_streamed_response_wrapper(
            browser.create_session,
        )


class AsyncBrowserResourceWithStreamingResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

        self.create_session = async_to_streamed_response_wrapper(
            browser.create_session,
        )
