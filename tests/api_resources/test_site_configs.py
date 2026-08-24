# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    LookupResponse,
    AnalysisSummary,
    SiteConfigResponse,
    RecommendationSummary,
)
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSiteConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        site_config = client.site_configs.retrieve(
            "id",
        )
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.site_configs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = response.parse()
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.site_configs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = response.parse()
            assert_matches_type(SiteConfigResponse, site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.site_configs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        site_config = client.site_configs.list()
        assert_matches_type(SyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        site_config = client.site_configs.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.site_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = response.parse()
        assert_matches_type(SyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.site_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = response.parse()
            assert_matches_type(SyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recommendations(self, client: Kernel) -> None:
        site_config = client.site_configs.list_recommendations()
        assert_matches_type(SyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recommendations_with_all_params(self, client: Kernel) -> None:
        site_config = client.site_configs.list_recommendations(
            limit=1,
            offset=0,
            sort_by="target",
            sort_order="asc",
        )
        assert_matches_type(SyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_recommendations(self, client: Kernel) -> None:
        response = client.site_configs.with_raw_response.list_recommendations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = response.parse()
        assert_matches_type(SyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_recommendations(self, client: Kernel) -> None:
        with client.site_configs.with_streaming_response.list_recommendations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = response.parse()
            assert_matches_type(SyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup(self, client: Kernel) -> None:
        site_config = client.site_configs.lookup(
            url="https://example.com",
        )
        assert_matches_type(LookupResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_with_all_params(self, client: Kernel) -> None:
        site_config = client.site_configs.lookup(
            url="https://example.com",
            allowed_proxy_countries=["US"],
        )
        assert_matches_type(LookupResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup(self, client: Kernel) -> None:
        response = client.site_configs.with_raw_response.lookup(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = response.parse()
        assert_matches_type(LookupResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup(self, client: Kernel) -> None:
        with client.site_configs.with_streaming_response.lookup(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = response.parse()
            assert_matches_type(LookupResponse, site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve(self, client: Kernel) -> None:
        site_config = client.site_configs.resolve(
            url="https://example.com",
        )
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve_with_all_params(self, client: Kernel) -> None:
        site_config = client.site_configs.resolve(
            url="https://example.com",
            allowed_proxy_countries=["US"],
        )
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resolve(self, client: Kernel) -> None:
        response = client.site_configs.with_raw_response.resolve(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = response.parse()
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resolve(self, client: Kernel) -> None:
        with client.site_configs.with_streaming_response.resolve(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = response.parse()
            assert_matches_type(SiteConfigResponse, site_config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSiteConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.retrieve(
            "id",
        )
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.site_configs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = await response.parse()
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.site_configs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = await response.parse()
            assert_matches_type(SiteConfigResponse, site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.site_configs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.list()
        assert_matches_type(AsyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.site_configs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = await response.parse()
        assert_matches_type(AsyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.site_configs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = await response.parse()
            assert_matches_type(AsyncOffsetPagination[AnalysisSummary], site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recommendations(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.list_recommendations()
        assert_matches_type(AsyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recommendations_with_all_params(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.list_recommendations(
            limit=1,
            offset=0,
            sort_by="target",
            sort_order="asc",
        )
        assert_matches_type(AsyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_recommendations(self, async_client: AsyncKernel) -> None:
        response = await async_client.site_configs.with_raw_response.list_recommendations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = await response.parse()
        assert_matches_type(AsyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_recommendations(self, async_client: AsyncKernel) -> None:
        async with async_client.site_configs.with_streaming_response.list_recommendations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = await response.parse()
            assert_matches_type(AsyncOffsetPagination[RecommendationSummary], site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.lookup(
            url="https://example.com",
        )
        assert_matches_type(LookupResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.lookup(
            url="https://example.com",
            allowed_proxy_countries=["US"],
        )
        assert_matches_type(LookupResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncKernel) -> None:
        response = await async_client.site_configs.with_raw_response.lookup(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = await response.parse()
        assert_matches_type(LookupResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncKernel) -> None:
        async with async_client.site_configs.with_streaming_response.lookup(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = await response.parse()
            assert_matches_type(LookupResponse, site_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.resolve(
            url="https://example.com",
        )
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncKernel) -> None:
        site_config = await async_client.site_configs.resolve(
            url="https://example.com",
            allowed_proxy_countries=["US"],
        )
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncKernel) -> None:
        response = await async_client.site_configs.with_raw_response.resolve(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_config = await response.parse()
        assert_matches_type(SiteConfigResponse, site_config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncKernel) -> None:
        async with async_client.site_configs.with_streaming_response.resolve(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_config = await response.parse()
            assert_matches_type(SiteConfigResponse, site_config, path=["response"])

        assert cast(Any, response.is_closed) is True
