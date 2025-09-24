# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from .fs.fs import (
    FsResource,
    AsyncFsResource,
    FsResourceWithRawResponse,
    AsyncFsResourceWithRawResponse,
    FsResourceWithStreamingResponse,
    AsyncFsResourceWithStreamingResponse,
)
from ...types import browser_create_params, browser_delete_params
from .process import (
    ProcessResource,
    AsyncProcessResource,
    ProcessResourceWithRawResponse,
    AsyncProcessResourceWithRawResponse,
    ProcessResourceWithStreamingResponse,
    AsyncProcessResourceWithStreamingResponse,
)
from .replays import (
    ReplaysResource,
    AsyncReplaysResource,
    ReplaysResourceWithRawResponse,
    AsyncReplaysResourceWithRawResponse,
    ReplaysResourceWithStreamingResponse,
    AsyncReplaysResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.browser_list_response import BrowserListResponse
from ...types.browser_create_response import BrowserCreateResponse
from ...types.browser_persistence_param import BrowserPersistenceParam
from ...types.browser_retrieve_response import BrowserRetrieveResponse

__all__ = ["BrowsersResource", "AsyncBrowsersResource"]


class BrowsersResource(SyncAPIResource):
    @cached_property
    def replays(self) -> ReplaysResource:
        return ReplaysResource(self._client)

    @cached_property
    def fs(self) -> FsResource:
        return FsResource(self._client)

    @cached_property
    def process(self) -> ProcessResource:
        return ProcessResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

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
        headless: bool | Omit = omit,
        invocation_id: str | Omit = omit,
        persistence: BrowserPersistenceParam | Omit = omit,
        profile: browser_create_params.Profile | Omit = omit,
        proxy_id: str | Omit = omit,
        stealth: bool | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserCreateResponse:
        """
        Create a new browser session from within an action.

        Args:
          headless: If true, launches the browser using a headless image (no VNC/GUI). Defaults to
              false.

          invocation_id: action invocation ID

          persistence: Optional persistence configuration for the browser session.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: The number of seconds of inactivity before the browser session is terminated.
              Only applicable to non-persistent browsers. Activity includes CDP connections
              and live view connections. Defaults to 60 seconds. Minimum allowed is 10
              seconds. Maximum allowed is 86400 (24 hours). We check for inactivity every 5
              seconds, so the actual timeout behavior you will see is +/- 5 seconds around the
              specified value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/browsers",
            body=maybe_transform(
                {
                    "headless": headless,
                    "invocation_id": invocation_id,
                    "persistence": persistence,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                },
                browser_create_params.BrowserCreateParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserRetrieveResponse:
        """
        Get information about a browser session.

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserListResponse:
        """List active browser sessions"""
        return self._get(
            "/browsers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserListResponse,
        )

    def delete(
        self,
        *,
        persistent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a persistent browser session by its persistent_id.

        Args:
          persistent_id: Persistent browser identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/browsers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"persistent_id": persistent_id}, browser_delete_params.BrowserDeleteParams),
            ),
            cast_to=NoneType,
        )

    def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a browser session by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBrowsersResource(AsyncAPIResource):
    @cached_property
    def replays(self) -> AsyncReplaysResource:
        return AsyncReplaysResource(self._client)

    @cached_property
    def fs(self) -> AsyncFsResource:
        return AsyncFsResource(self._client)

    @cached_property
    def process(self) -> AsyncProcessResource:
        return AsyncProcessResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

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
        headless: bool | Omit = omit,
        invocation_id: str | Omit = omit,
        persistence: BrowserPersistenceParam | Omit = omit,
        profile: browser_create_params.Profile | Omit = omit,
        proxy_id: str | Omit = omit,
        stealth: bool | Omit = omit,
        timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserCreateResponse:
        """
        Create a new browser session from within an action.

        Args:
          headless: If true, launches the browser using a headless image (no VNC/GUI). Defaults to
              false.

          invocation_id: action invocation ID

          persistence: Optional persistence configuration for the browser session.

          profile: Profile selection for the browser session. Provide either id or name. If
              specified, the matching profile will be loaded into the browser session.
              Profiles must be created beforehand.

          proxy_id: Optional proxy to associate to the browser session. Must reference a proxy
              belonging to the caller's org.

          stealth: If true, launches the browser in stealth mode to reduce detection by anti-bot
              mechanisms.

          timeout_seconds: The number of seconds of inactivity before the browser session is terminated.
              Only applicable to non-persistent browsers. Activity includes CDP connections
              and live view connections. Defaults to 60 seconds. Minimum allowed is 10
              seconds. Maximum allowed is 86400 (24 hours). We check for inactivity every 5
              seconds, so the actual timeout behavior you will see is +/- 5 seconds around the
              specified value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/browsers",
            body=await async_maybe_transform(
                {
                    "headless": headless,
                    "invocation_id": invocation_id,
                    "persistence": persistence,
                    "profile": profile,
                    "proxy_id": proxy_id,
                    "stealth": stealth,
                    "timeout_seconds": timeout_seconds,
                },
                browser_create_params.BrowserCreateParams,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserRetrieveResponse:
        """
        Get information about a browser session.

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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserListResponse:
        """List active browser sessions"""
        return await self._get(
            "/browsers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserListResponse,
        )

    async def delete(
        self,
        *,
        persistent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a persistent browser session by its persistent_id.

        Args:
          persistent_id: Persistent browser identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/browsers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"persistent_id": persistent_id}, browser_delete_params.BrowserDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a browser session by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/browsers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        self.list = to_raw_response_wrapper(
            browsers.list,
        )
        self.delete = to_raw_response_wrapper(
            browsers.delete,
        )
        self.delete_by_id = to_raw_response_wrapper(
            browsers.delete_by_id,
        )

    @cached_property
    def replays(self) -> ReplaysResourceWithRawResponse:
        return ReplaysResourceWithRawResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> FsResourceWithRawResponse:
        return FsResourceWithRawResponse(self._browsers.fs)

    @cached_property
    def process(self) -> ProcessResourceWithRawResponse:
        return ProcessResourceWithRawResponse(self._browsers.process)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._browsers.logs)


class AsyncBrowsersResourceWithRawResponse:
    def __init__(self, browsers: AsyncBrowsersResource) -> None:
        self._browsers = browsers

        self.create = async_to_raw_response_wrapper(
            browsers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            browsers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            browsers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            browsers.delete,
        )
        self.delete_by_id = async_to_raw_response_wrapper(
            browsers.delete_by_id,
        )

    @cached_property
    def replays(self) -> AsyncReplaysResourceWithRawResponse:
        return AsyncReplaysResourceWithRawResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> AsyncFsResourceWithRawResponse:
        return AsyncFsResourceWithRawResponse(self._browsers.fs)

    @cached_property
    def process(self) -> AsyncProcessResourceWithRawResponse:
        return AsyncProcessResourceWithRawResponse(self._browsers.process)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._browsers.logs)


class BrowsersResourceWithStreamingResponse:
    def __init__(self, browsers: BrowsersResource) -> None:
        self._browsers = browsers

        self.create = to_streamed_response_wrapper(
            browsers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            browsers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            browsers.list,
        )
        self.delete = to_streamed_response_wrapper(
            browsers.delete,
        )
        self.delete_by_id = to_streamed_response_wrapper(
            browsers.delete_by_id,
        )

    @cached_property
    def replays(self) -> ReplaysResourceWithStreamingResponse:
        return ReplaysResourceWithStreamingResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> FsResourceWithStreamingResponse:
        return FsResourceWithStreamingResponse(self._browsers.fs)

    @cached_property
    def process(self) -> ProcessResourceWithStreamingResponse:
        return ProcessResourceWithStreamingResponse(self._browsers.process)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._browsers.logs)


class AsyncBrowsersResourceWithStreamingResponse:
    def __init__(self, browsers: AsyncBrowsersResource) -> None:
        self._browsers = browsers

        self.create = async_to_streamed_response_wrapper(
            browsers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            browsers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            browsers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            browsers.delete,
        )
        self.delete_by_id = async_to_streamed_response_wrapper(
            browsers.delete_by_id,
        )

    @cached_property
    def replays(self) -> AsyncReplaysResourceWithStreamingResponse:
        return AsyncReplaysResourceWithStreamingResponse(self._browsers.replays)

    @cached_property
    def fs(self) -> AsyncFsResourceWithStreamingResponse:
        return AsyncFsResourceWithStreamingResponse(self._browsers.fs)

    @cached_property
    def process(self) -> AsyncProcessResourceWithStreamingResponse:
        return AsyncProcessResourceWithStreamingResponse(self._browsers.process)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._browsers.logs)
