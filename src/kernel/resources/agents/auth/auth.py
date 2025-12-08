# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .invocations import (
    InvocationsResource,
    AsyncInvocationsResource,
    InvocationsResourceWithRawResponse,
    AsyncInvocationsResourceWithRawResponse,
    InvocationsResourceWithStreamingResponse,
    AsyncInvocationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPagination, AsyncOffsetPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.agents import auth_list_params, auth_create_params
from ....types.agents.auth_agent import AuthAgent

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def invocations(self) -> InvocationsResource:
        return InvocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        profile_name: str,
        target_domain: str,
        login_url: str | Omit = omit,
        proxy: auth_create_params.Proxy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthAgent:
        """
        Creates a new auth agent for the specified domain and profile combination, or
        returns an existing one if it already exists. This is idempotent - calling with
        the same domain and profile will return the same agent. Does NOT start an
        invocation - use POST /agents/auth/invocations to start an auth flow.

        Args:
          profile_name: Name of the profile to use for this auth agent

          target_domain: Target domain for authentication

          login_url: Optional login page URL. If provided, will be stored on the agent and used to
              skip discovery in future invocations.

          proxy: Optional proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/auth",
            body=maybe_transform(
                {
                    "profile_name": profile_name,
                    "target_domain": target_domain,
                    "login_url": login_url,
                    "proxy": proxy,
                },
                auth_create_params.AuthCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAgent,
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
    ) -> AuthAgent:
        """Retrieve an auth agent by its ID.

        Returns the current authentication status of
        the managed profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/agents/auth/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAgent,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        profile_name: str | Omit = omit,
        target_domain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[AuthAgent]:
        """
        List auth agents with optional filters for profile_name and target_domain.

        Args:
          limit: Maximum number of results to return

          offset: Number of results to skip

          profile_name: Filter by profile name

          target_domain: Filter by target domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agents/auth",
            page=SyncOffsetPagination[AuthAgent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "profile_name": profile_name,
                        "target_domain": target_domain,
                    },
                    auth_list_params.AuthListParams,
                ),
            ),
            model=AuthAgent,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def invocations(self) -> AsyncInvocationsResource:
        return AsyncInvocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        profile_name: str,
        target_domain: str,
        login_url: str | Omit = omit,
        proxy: auth_create_params.Proxy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthAgent:
        """
        Creates a new auth agent for the specified domain and profile combination, or
        returns an existing one if it already exists. This is idempotent - calling with
        the same domain and profile will return the same agent. Does NOT start an
        invocation - use POST /agents/auth/invocations to start an auth flow.

        Args:
          profile_name: Name of the profile to use for this auth agent

          target_domain: Target domain for authentication

          login_url: Optional login page URL. If provided, will be stored on the agent and used to
              skip discovery in future invocations.

          proxy: Optional proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/auth",
            body=await async_maybe_transform(
                {
                    "profile_name": profile_name,
                    "target_domain": target_domain,
                    "login_url": login_url,
                    "proxy": proxy,
                },
                auth_create_params.AuthCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAgent,
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
    ) -> AuthAgent:
        """Retrieve an auth agent by its ID.

        Returns the current authentication status of
        the managed profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/agents/auth/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAgent,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        profile_name: str | Omit = omit,
        target_domain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuthAgent, AsyncOffsetPagination[AuthAgent]]:
        """
        List auth agents with optional filters for profile_name and target_domain.

        Args:
          limit: Maximum number of results to return

          offset: Number of results to skip

          profile_name: Filter by profile name

          target_domain: Filter by target domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agents/auth",
            page=AsyncOffsetPagination[AuthAgent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "profile_name": profile_name,
                        "target_domain": target_domain,
                    },
                    auth_list_params.AuthListParams,
                ),
            ),
            model=AuthAgent,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.create = to_raw_response_wrapper(
            auth.create,
        )
        self.retrieve = to_raw_response_wrapper(
            auth.retrieve,
        )
        self.list = to_raw_response_wrapper(
            auth.list,
        )

    @cached_property
    def invocations(self) -> InvocationsResourceWithRawResponse:
        return InvocationsResourceWithRawResponse(self._auth.invocations)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.create = async_to_raw_response_wrapper(
            auth.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            auth.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            auth.list,
        )

    @cached_property
    def invocations(self) -> AsyncInvocationsResourceWithRawResponse:
        return AsyncInvocationsResourceWithRawResponse(self._auth.invocations)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.create = to_streamed_response_wrapper(
            auth.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            auth.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            auth.list,
        )

    @cached_property
    def invocations(self) -> InvocationsResourceWithStreamingResponse:
        return InvocationsResourceWithStreamingResponse(self._auth.invocations)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.create = async_to_streamed_response_wrapper(
            auth.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            auth.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            auth.list,
        )

    @cached_property
    def invocations(self) -> AsyncInvocationsResourceWithStreamingResponse:
        return AsyncInvocationsResourceWithStreamingResponse(self._auth.invocations)
