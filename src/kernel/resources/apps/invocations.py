# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.apps import invocation_create_params, invocation_update_params
from ..._base_client import make_request_options
from ...types.apps.invocation_create_response import InvocationCreateResponse
from ...types.apps.invocation_update_response import InvocationUpdateResponse
from ...types.apps.invocation_retrieve_response import InvocationRetrieveResponse

__all__ = ["InvocationsResource", "AsyncInvocationsResource"]


class InvocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return InvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return InvocationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action_name: str,
        app_name: str,
        version: str,
        async_: bool | NotGiven = NOT_GIVEN,
        payload: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvocationCreateResponse:
        """
        Invoke an action.

        Args:
          action_name: Name of the action to invoke

          app_name: Name of the application

          version: Version of the application

          async_: If true, invoke asynchronously. When set, the API responds 202 Accepted with
              status "queued".

          payload: Input data for the action, sent as a JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/invocations",
            body=maybe_transform(
                {
                    "action_name": action_name,
                    "app_name": app_name,
                    "version": version,
                    "async_": async_,
                    "payload": payload,
                },
                invocation_create_params.InvocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationCreateResponse,
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
    ) -> InvocationRetrieveResponse:
        """
        Get details about an invocation's status and output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/invocations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["succeeded", "failed"],
        output: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvocationUpdateResponse:
        """
        Update an invocation's status or output.

        Args:
          status: New status for the invocation.

          output: Updated output of the invocation rendered as JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/invocations/{id}",
            body=maybe_transform(
                {
                    "status": status,
                    "output": output,
                },
                invocation_update_params.InvocationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationUpdateResponse,
        )


class AsyncInvocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInvocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncInvocationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action_name: str,
        app_name: str,
        version: str,
        async_: bool | NotGiven = NOT_GIVEN,
        payload: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvocationCreateResponse:
        """
        Invoke an action.

        Args:
          action_name: Name of the action to invoke

          app_name: Name of the application

          version: Version of the application

          async_: If true, invoke asynchronously. When set, the API responds 202 Accepted with
              status "queued".

          payload: Input data for the action, sent as a JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/invocations",
            body=await async_maybe_transform(
                {
                    "action_name": action_name,
                    "app_name": app_name,
                    "version": version,
                    "async_": async_,
                    "payload": payload,
                },
                invocation_create_params.InvocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationCreateResponse,
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
    ) -> InvocationRetrieveResponse:
        """
        Get details about an invocation's status and output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/invocations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["succeeded", "failed"],
        output: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvocationUpdateResponse:
        """
        Update an invocation's status or output.

        Args:
          status: New status for the invocation.

          output: Updated output of the invocation rendered as JSON string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/invocations/{id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "output": output,
                },
                invocation_update_params.InvocationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvocationUpdateResponse,
        )


class InvocationsResourceWithRawResponse:
    def __init__(self, invocations: InvocationsResource) -> None:
        self._invocations = invocations

        self.create = to_raw_response_wrapper(
            invocations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invocations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            invocations.update,
        )


class AsyncInvocationsResourceWithRawResponse:
    def __init__(self, invocations: AsyncInvocationsResource) -> None:
        self._invocations = invocations

        self.create = async_to_raw_response_wrapper(
            invocations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invocations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            invocations.update,
        )


class InvocationsResourceWithStreamingResponse:
    def __init__(self, invocations: InvocationsResource) -> None:
        self._invocations = invocations

        self.create = to_streamed_response_wrapper(
            invocations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invocations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            invocations.update,
        )


class AsyncInvocationsResourceWithStreamingResponse:
    def __init__(self, invocations: AsyncInvocationsResource) -> None:
        self._invocations = invocations

        self.create = async_to_streamed_response_wrapper(
            invocations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invocations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            invocations.update,
        )
