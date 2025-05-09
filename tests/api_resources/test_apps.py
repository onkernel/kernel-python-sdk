# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    AppDeployResponse,
    AppInvokeResponse,
    AppRetrieveInvocationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_deploy(self, client: Kernel) -> None:
        app = client.apps.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
        )
        assert_matches_type(AppDeployResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_deploy_with_all_params(self, client: Kernel) -> None:
        app = client.apps.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
            region="aws.us-east-1a",
        )
        assert_matches_type(AppDeployResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_deploy(self, client: Kernel) -> None:
        response = client.apps.with_raw_response.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppDeployResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_deploy(self, client: Kernel) -> None:
        with client.apps.with_streaming_response.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppDeployResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_invoke(self, client: Kernel) -> None:
        app = client.apps.invoke(
            action_name="analyze",
            app_name="my-awesome-app",
            payload='{ "data": "example input" }',
            version="1.0.0",
        )
        assert_matches_type(AppInvokeResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_invoke(self, client: Kernel) -> None:
        response = client.apps.with_raw_response.invoke(
            action_name="analyze",
            app_name="my-awesome-app",
            payload='{ "data": "example input" }',
            version="1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppInvokeResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_invoke(self, client: Kernel) -> None:
        with client.apps.with_streaming_response.invoke(
            action_name="analyze",
            app_name="my-awesome-app",
            payload='{ "data": "example input" }',
            version="1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppInvokeResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_invocation(self, client: Kernel) -> None:
        app = client.apps.retrieve_invocation(
            "id",
        )
        assert_matches_type(AppRetrieveInvocationResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_invocation(self, client: Kernel) -> None:
        response = client.apps.with_raw_response.retrieve_invocation(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppRetrieveInvocationResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_invocation(self, client: Kernel) -> None:
        with client.apps.with_streaming_response.retrieve_invocation(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppRetrieveInvocationResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_invocation(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.apps.with_raw_response.retrieve_invocation(
                "",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_deploy(self, async_client: AsyncKernel) -> None:
        app = await async_client.apps.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
        )
        assert_matches_type(AppDeployResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_deploy_with_all_params(self, async_client: AsyncKernel) -> None:
        app = await async_client.apps.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
            region="aws.us-east-1a",
        )
        assert_matches_type(AppDeployResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_deploy(self, async_client: AsyncKernel) -> None:
        response = await async_client.apps.with_raw_response.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppDeployResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_deploy(self, async_client: AsyncKernel) -> None:
        async with async_client.apps.with_streaming_response.deploy(
            app_name="my-awesome-app",
            file=b"raw file contents",
            version="1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppDeployResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_invoke(self, async_client: AsyncKernel) -> None:
        app = await async_client.apps.invoke(
            action_name="analyze",
            app_name="my-awesome-app",
            payload='{ "data": "example input" }',
            version="1.0.0",
        )
        assert_matches_type(AppInvokeResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_invoke(self, async_client: AsyncKernel) -> None:
        response = await async_client.apps.with_raw_response.invoke(
            action_name="analyze",
            app_name="my-awesome-app",
            payload='{ "data": "example input" }',
            version="1.0.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppInvokeResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_invoke(self, async_client: AsyncKernel) -> None:
        async with async_client.apps.with_streaming_response.invoke(
            action_name="analyze",
            app_name="my-awesome-app",
            payload='{ "data": "example input" }',
            version="1.0.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppInvokeResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_invocation(self, async_client: AsyncKernel) -> None:
        app = await async_client.apps.retrieve_invocation(
            "id",
        )
        assert_matches_type(AppRetrieveInvocationResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_invocation(self, async_client: AsyncKernel) -> None:
        response = await async_client.apps.with_raw_response.retrieve_invocation(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppRetrieveInvocationResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_invocation(self, async_client: AsyncKernel) -> None:
        async with async_client.apps.with_streaming_response.retrieve_invocation(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppRetrieveInvocationResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_invocation(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.apps.with_raw_response.retrieve_invocation(
                "",
            )
