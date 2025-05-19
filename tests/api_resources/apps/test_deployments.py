# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.types.apps import DeploymentCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        deployment = client.apps.deployments.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        deployment = client.apps.deployments.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
            force=False,
            region="aws.us-east-1a",
            version="1.0.0",
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.apps.deployments.with_raw_response.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.apps.deployments.with_streaming_response.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        deployment = await async_client.apps.deployments.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        deployment = await async_client.apps.deployments.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
            force=False,
            region="aws.us-east-1a",
            version="1.0.0",
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.apps.deployments.with_raw_response.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.apps.deployments.with_streaming_response.create(
            entrypoint_rel_path="src/app.py",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True
