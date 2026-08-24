# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    site_config_list_params,
    site_config_lookup_params,
    site_config_resolve_params,
    site_config_list_recommendations_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.lookup_response import LookupResponse
from ..types.analysis_summary import AnalysisSummary
from ..types.site_config_response import SiteConfigResponse
from ..types.recommendation_summary import RecommendationSummary

__all__ = ["SiteConfigsResource", "AsyncSiteConfigsResource"]


class SiteConfigsResource(SyncAPIResource):
    """Resolve browser and proxy recommendations for bot-protected sites."""

    @cached_property
    def with_raw_response(self) -> SiteConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SiteConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SiteConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return SiteConfigsResourceWithStreamingResponse(self)

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
    ) -> SiteConfigResponse:
        """
        Returns a project-scoped historical analysis and the recommendation outcome
        concluded by that run. Later knowledge does not change this response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/site-configs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiteConfigResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[AnalysisSummary]:
        """
        Lists analyses for the selected project, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/site-configs",
            page=SyncOffsetPagination[AnalysisSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    site_config_list_params.SiteConfigListParams,
                ),
            ),
            model=AnalysisSummary,
        )

    def list_recommendations(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["target", "recommended_config", "last_requested_at", "success_rate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[RecommendationSummary]:
        """
        Lists unique domains previously analyzed by the selected project with their
        current domain-level recommendations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/site-configs/recommendations",
            page=SyncOffsetPagination[RecommendationSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    site_config_list_recommendations_params.SiteConfigListRecommendationsParams,
                ),
            ),
            model=RecommendationSummary,
        )

    def lookup(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupResponse:
        """
        Returns current global knowledge without resolving DNS, creating an analysis, or
        updating Site Config data.

        Args:
          url: Public HTTP(S) URL to look up.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when returning a proxy configuration. When
              omitted, Kernel uses its default country selection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/site-configs/lookup",
            body=maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                },
                site_config_lookup_params.SiteConfigLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupResponse,
        )

    def resolve(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SiteConfigResponse:
        """
        Explicitly starts or retries a project-scoped background analysis while
        preserving current global knowledge when available. Use `/site-configs/lookup`
        for side-effect-free reads.

        Args:
          url: Public HTTP(S) URL to refresh.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when searching for or returning a proxy
              configuration. Kernel may test a subset of allowed countries. When omitted,
              Kernel uses its default country selection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/site-configs/resolve",
            body=maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                },
                site_config_resolve_params.SiteConfigResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiteConfigResponse,
        )


class AsyncSiteConfigsResource(AsyncAPIResource):
    """Resolve browser and proxy recommendations for bot-protected sites."""

    @cached_property
    def with_raw_response(self) -> AsyncSiteConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSiteConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSiteConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncSiteConfigsResourceWithStreamingResponse(self)

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
    ) -> SiteConfigResponse:
        """
        Returns a project-scoped historical analysis and the recommendation outcome
        concluded by that run. Later knowledge does not change this response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/site-configs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiteConfigResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AnalysisSummary, AsyncOffsetPagination[AnalysisSummary]]:
        """
        Lists analyses for the selected project, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/site-configs",
            page=AsyncOffsetPagination[AnalysisSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    site_config_list_params.SiteConfigListParams,
                ),
            ),
            model=AnalysisSummary,
        )

    def list_recommendations(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["target", "recommended_config", "last_requested_at", "success_rate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RecommendationSummary, AsyncOffsetPagination[RecommendationSummary]]:
        """
        Lists unique domains previously analyzed by the selected project with their
        current domain-level recommendations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/site-configs/recommendations",
            page=AsyncOffsetPagination[RecommendationSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    site_config_list_recommendations_params.SiteConfigListRecommendationsParams,
                ),
            ),
            model=RecommendationSummary,
        )

    async def lookup(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupResponse:
        """
        Returns current global knowledge without resolving DNS, creating an analysis, or
        updating Site Config data.

        Args:
          url: Public HTTP(S) URL to look up.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when returning a proxy configuration. When
              omitted, Kernel uses its default country selection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/site-configs/lookup",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                },
                site_config_lookup_params.SiteConfigLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupResponse,
        )

    async def resolve(
        self,
        *,
        url: str,
        allowed_proxy_countries: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SiteConfigResponse:
        """
        Explicitly starts or retries a project-scoped background analysis while
        preserving current global knowledge when available. Use `/site-configs/lookup`
        for side-effect-free reads.

        Args:
          url: Public HTTP(S) URL to refresh.

          allowed_proxy_countries: ISO 3166 country codes Kernel may use when searching for or returning a proxy
              configuration. Kernel may test a subset of allowed countries. When omitted,
              Kernel uses its default country selection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/site-configs/resolve",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "allowed_proxy_countries": allowed_proxy_countries,
                },
                site_config_resolve_params.SiteConfigResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiteConfigResponse,
        )


class SiteConfigsResourceWithRawResponse:
    def __init__(self, site_configs: SiteConfigsResource) -> None:
        self._site_configs = site_configs

        self.retrieve = to_raw_response_wrapper(
            site_configs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            site_configs.list,
        )
        self.list_recommendations = to_raw_response_wrapper(
            site_configs.list_recommendations,
        )
        self.lookup = to_raw_response_wrapper(
            site_configs.lookup,
        )
        self.resolve = to_raw_response_wrapper(
            site_configs.resolve,
        )


class AsyncSiteConfigsResourceWithRawResponse:
    def __init__(self, site_configs: AsyncSiteConfigsResource) -> None:
        self._site_configs = site_configs

        self.retrieve = async_to_raw_response_wrapper(
            site_configs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            site_configs.list,
        )
        self.list_recommendations = async_to_raw_response_wrapper(
            site_configs.list_recommendations,
        )
        self.lookup = async_to_raw_response_wrapper(
            site_configs.lookup,
        )
        self.resolve = async_to_raw_response_wrapper(
            site_configs.resolve,
        )


class SiteConfigsResourceWithStreamingResponse:
    def __init__(self, site_configs: SiteConfigsResource) -> None:
        self._site_configs = site_configs

        self.retrieve = to_streamed_response_wrapper(
            site_configs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            site_configs.list,
        )
        self.list_recommendations = to_streamed_response_wrapper(
            site_configs.list_recommendations,
        )
        self.lookup = to_streamed_response_wrapper(
            site_configs.lookup,
        )
        self.resolve = to_streamed_response_wrapper(
            site_configs.resolve,
        )


class AsyncSiteConfigsResourceWithStreamingResponse:
    def __init__(self, site_configs: AsyncSiteConfigsResource) -> None:
        self._site_configs = site_configs

        self.retrieve = async_to_streamed_response_wrapper(
            site_configs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            site_configs.list,
        )
        self.list_recommendations = async_to_streamed_response_wrapper(
            site_configs.list_recommendations,
        )
        self.lookup = async_to_streamed_response_wrapper(
            site_configs.lookup,
        )
        self.resolve = async_to_streamed_response_wrapper(
            site_configs.resolve,
        )
