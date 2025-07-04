# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    BrowserListResponse,
    BrowserCreateResponse,
    BrowserRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        browser = client.browsers.create()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        browser = client.browsers.create(
            headless=False,
            invocation_id="rr33xuugxj9h0bkf1rdt2bet",
            persistence={"id": "my-awesome-browser-for-user-1234"},
            stealth=True,
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserCreateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        browser = client.browsers.retrieve(
            "id",
        )
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        browser = client.browsers.list()
        assert_matches_type(BrowserListResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserListResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserListResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        browser = client.browsers.delete(
            persistent_id="persistent_id",
        )
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.delete(
            persistent_id="persistent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.delete(
            persistent_id="persistent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_by_id(self, client: Kernel) -> None:
        browser = client.browsers.delete_by_id(
            "id",
        )
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_by_id(self, client: Kernel) -> None:
        response = client.browsers.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_by_id(self, client: Kernel) -> None:
        with client.browsers.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_by_id(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browsers.with_raw_response.delete_by_id(
                "",
            )


class TestAsyncBrowsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.create()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.create(
            headless=False,
            invocation_id="rr33xuugxj9h0bkf1rdt2bet",
            persistence={"id": "my-awesome-browser-for-user-1234"},
            stealth=True,
        )
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserCreateResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserCreateResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.retrieve(
            "id",
        )
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserRetrieveResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.list()
        assert_matches_type(BrowserListResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserListResponse, browser, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserListResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.delete(
            persistent_id="persistent_id",
        )
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.delete(
            persistent_id="persistent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.delete(
            persistent_id="persistent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncKernel) -> None:
        browser = await async_client.browsers.delete_by_id(
            "id",
        )
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncKernel) -> None:
        response = await async_client.browsers.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert browser is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncKernel) -> None:
        async with async_client.browsers.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert browser is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browsers.with_raw_response.delete_by_id(
                "",
            )
