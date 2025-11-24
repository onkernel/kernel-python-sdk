# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.agents import AgentAuthRunResponse, AgentAuthSubmitResponse, AgentAuthDiscoverResponse
from kernel.types.agents.auth import RunExchangeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        run = client.agents.auth.runs.retrieve(
            "run_id",
        )
        assert_matches_type(AgentAuthRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.agents.auth.runs.with_raw_response.retrieve(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(AgentAuthRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.agents.auth.runs.with_streaming_response.retrieve(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(AgentAuthRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agents.auth.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_discover(self, client: Kernel) -> None:
        run = client.agents.auth.runs.discover(
            "run_id",
        )
        assert_matches_type(AgentAuthDiscoverResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_discover(self, client: Kernel) -> None:
        response = client.agents.auth.runs.with_raw_response.discover(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(AgentAuthDiscoverResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_discover(self, client: Kernel) -> None:
        with client.agents.auth.runs.with_streaming_response.discover(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(AgentAuthDiscoverResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_discover(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agents.auth.runs.with_raw_response.discover(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_exchange(self, client: Kernel) -> None:
        run = client.agents.auth.runs.exchange(
            run_id="run_id",
            code="otp_abc123xyz",
        )
        assert_matches_type(RunExchangeResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_exchange(self, client: Kernel) -> None:
        response = client.agents.auth.runs.with_raw_response.exchange(
            run_id="run_id",
            code="otp_abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunExchangeResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_exchange(self, client: Kernel) -> None:
        with client.agents.auth.runs.with_streaming_response.exchange(
            run_id="run_id",
            code="otp_abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunExchangeResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_exchange(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agents.auth.runs.with_raw_response.exchange(
                run_id="",
                code="otp_abc123xyz",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit(self, client: Kernel) -> None:
        run = client.agents.auth.runs.submit(
            run_id="run_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )
        assert_matches_type(AgentAuthSubmitResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Kernel) -> None:
        response = client.agents.auth.runs.with_raw_response.submit(
            run_id="run_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(AgentAuthSubmitResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Kernel) -> None:
        with client.agents.auth.runs.with_streaming_response.submit(
            run_id="run_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(AgentAuthSubmitResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agents.auth.runs.with_raw_response.submit(
                run_id="",
                field_values={
                    "email": "user@example.com",
                    "password": "********",
                },
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        run = await async_client.agents.auth.runs.retrieve(
            "run_id",
        )
        assert_matches_type(AgentAuthRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.runs.with_raw_response.retrieve(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AgentAuthRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.runs.with_streaming_response.retrieve(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AgentAuthRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agents.auth.runs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_discover(self, async_client: AsyncKernel) -> None:
        run = await async_client.agents.auth.runs.discover(
            "run_id",
        )
        assert_matches_type(AgentAuthDiscoverResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.runs.with_raw_response.discover(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AgentAuthDiscoverResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.runs.with_streaming_response.discover(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AgentAuthDiscoverResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_discover(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agents.auth.runs.with_raw_response.discover(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_exchange(self, async_client: AsyncKernel) -> None:
        run = await async_client.agents.auth.runs.exchange(
            run_id="run_id",
            code="otp_abc123xyz",
        )
        assert_matches_type(RunExchangeResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_exchange(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.runs.with_raw_response.exchange(
            run_id="run_id",
            code="otp_abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunExchangeResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_exchange(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.runs.with_streaming_response.exchange(
            run_id="run_id",
            code="otp_abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunExchangeResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_exchange(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agents.auth.runs.with_raw_response.exchange(
                run_id="",
                code="otp_abc123xyz",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncKernel) -> None:
        run = await async_client.agents.auth.runs.submit(
            run_id="run_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )
        assert_matches_type(AgentAuthSubmitResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncKernel) -> None:
        response = await async_client.agents.auth.runs.with_raw_response.submit(
            run_id="run_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AgentAuthSubmitResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncKernel) -> None:
        async with async_client.agents.auth.runs.with_streaming_response.submit(
            run_id="run_id",
            field_values={
                "email": "user@example.com",
                "password": "********",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AgentAuthSubmitResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agents.auth.runs.with_raw_response.submit(
                run_id="",
                field_values={
                    "email": "user@example.com",
                    "password": "********",
                },
            )
