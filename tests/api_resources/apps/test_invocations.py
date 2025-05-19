# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.apps import InvocationCreateResponse, InvocationRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        invocation = client.apps.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        invocation = client.apps.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
            payload='{"data":"example input"}',
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.apps.invocations.with_raw_response.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.apps.invocations.with_streaming_response.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        invocation = client.apps.invocations.retrieve(
            "id",
        )
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.apps.invocations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.apps.invocations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.apps.invocations.with_raw_response.retrieve(
                "",
            )


class TestAsyncInvocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.apps.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.apps.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
            payload='{"data":"example input"}',
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.apps.invocations.with_raw_response.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.apps.invocations.with_streaming_response.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.apps.invocations.retrieve(
            "id",
        )
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.apps.invocations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.apps.invocations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.apps.invocations.with_raw_response.retrieve(
                "",
            )
