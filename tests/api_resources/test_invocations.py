# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types import (
    InvocationCreateResponse,
    InvocationUpdateResponse,
    InvocationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        invocation = client.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        invocation = client.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
            async_=True,
            payload='{"data":"example input"}',
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.invocations.with_raw_response.create(
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
        with client.invocations.with_streaming_response.create(
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
        invocation = client.invocations.retrieve(
            "id",
        )
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.invocations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.invocations.with_streaming_response.retrieve(
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
            client.invocations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        invocation = client.invocations.update(
            id="id",
            status="succeeded",
        )
        assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        invocation = client.invocations.update(
            id="id",
            status="succeeded",
            output="output",
        )
        assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.invocations.with_raw_response.update(
            id="id",
            status="succeeded",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.invocations.with_streaming_response.update(
            id="id",
            status="succeeded",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invocations.with_raw_response.update(
                id="",
                status="succeeded",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_browsers(self, client: Kernel) -> None:
        invocation = client.invocations.delete_browsers(
            "id",
        )
        assert invocation is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_browsers(self, client: Kernel) -> None:
        response = client.invocations.with_raw_response.delete_browsers(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = response.parse()
        assert invocation is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_browsers(self, client: Kernel) -> None:
        with client.invocations.with_streaming_response.delete_browsers(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = response.parse()
            assert invocation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_browsers(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invocations.with_raw_response.delete_browsers(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_method_follow(self, client: Kernel) -> None:
        invocation_stream = client.invocations.follow(
            "id",
        )
        invocation_stream.response.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_follow(self, client: Kernel) -> None:
        response = client.invocations.with_raw_response.follow(
            "id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_follow(self, client: Kernel) -> None:
        with client.invocations.with_streaming_response.follow(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    def test_path_params_follow(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invocations.with_raw_response.follow(
                "",
            )


class TestAsyncInvocations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.invocations.create(
            action_name="analyze",
            app_name="my-app",
            version="1.0.0",
            async_=True,
            payload='{"data":"example input"}',
        )
        assert_matches_type(InvocationCreateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.invocations.with_raw_response.create(
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
        async with async_client.invocations.with_streaming_response.create(
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
        invocation = await async_client.invocations.retrieve(
            "id",
        )
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.invocations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(InvocationRetrieveResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.invocations.with_streaming_response.retrieve(
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
            await async_client.invocations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.invocations.update(
            id="id",
            status="succeeded",
        )
        assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.invocations.update(
            id="id",
            status="succeeded",
            output="output",
        )
        assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.invocations.with_raw_response.update(
            id="id",
            status="succeeded",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.invocations.with_streaming_response.update(
            id="id",
            status="succeeded",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert_matches_type(InvocationUpdateResponse, invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invocations.with_raw_response.update(
                id="",
                status="succeeded",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_browsers(self, async_client: AsyncKernel) -> None:
        invocation = await async_client.invocations.delete_browsers(
            "id",
        )
        assert invocation is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_browsers(self, async_client: AsyncKernel) -> None:
        response = await async_client.invocations.with_raw_response.delete_browsers(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invocation = await response.parse()
        assert invocation is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_browsers(self, async_client: AsyncKernel) -> None:
        async with async_client.invocations.with_streaming_response.delete_browsers(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invocation = await response.parse()
            assert invocation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_browsers(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invocations.with_raw_response.delete_browsers(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_method_follow(self, async_client: AsyncKernel) -> None:
        invocation_stream = await async_client.invocations.follow(
            "id",
        )
        await invocation_stream.response.aclose()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_follow(self, async_client: AsyncKernel) -> None:
        response = await async_client.invocations.with_raw_response.follow(
            "id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_follow(self, async_client: AsyncKernel) -> None:
        async with async_client.invocations.with_streaming_response.follow(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type text/event-stream, Prism mock server will fail"
    )
    @parametrize
    async def test_path_params_follow(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invocations.with_raw_response.follow(
                "",
            )
