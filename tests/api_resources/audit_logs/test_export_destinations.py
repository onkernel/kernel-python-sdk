# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kernel import Kernel, AsyncKernel
from tests.utils import assert_matches_type
from kernel.pagination import SyncOffsetPagination, AsyncOffsetPagination
from kernel.types.audit_logs import (
    AuditLogExportDestination,
    AuditLogExportDestinationTestResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExportDestinations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
            kms_key_id="kms_key_id",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Kernel) -> None:
        response = client.audit_logs.export_destinations.with_raw_response.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = response.parse()
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Kernel) -> None:
        with client.audit_logs.export_destinations.with_streaming_response.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = response.parse()
            assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.retrieve(
            "id",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Kernel) -> None:
        response = client.audit_logs.export_destinations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = response.parse()
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Kernel) -> None:
        with client.audit_logs.export_destinations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = response.parse()
            assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.audit_logs.export_destinations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.update(
            id="id",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.update(
            id="id",
            bucket="xxx",
            kms_key_id="kms_key_id",
            prefix="prefix",
            region="x",
            role_arn="x",
            status="active",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Kernel) -> None:
        response = client.audit_logs.export_destinations.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = response.parse()
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Kernel) -> None:
        with client.audit_logs.export_destinations.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = response.parse()
            assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.audit_logs.export_destinations.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.list()
        assert_matches_type(SyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Kernel) -> None:
        response = client.audit_logs.export_destinations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = response.parse()
        assert_matches_type(SyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Kernel) -> None:
        with client.audit_logs.export_destinations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = response.parse()
            assert_matches_type(SyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.delete(
            "id",
        )
        assert export_destination is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Kernel) -> None:
        response = client.audit_logs.export_destinations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = response.parse()
        assert export_destination is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Kernel) -> None:
        with client.audit_logs.export_destinations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = response.parse()
            assert export_destination is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.audit_logs.export_destinations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Kernel) -> None:
        export_destination = client.audit_logs.export_destinations.test(
            "id",
        )
        assert_matches_type(AuditLogExportDestinationTestResult, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Kernel) -> None:
        response = client.audit_logs.export_destinations.with_raw_response.test(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = response.parse()
        assert_matches_type(AuditLogExportDestinationTestResult, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Kernel) -> None:
        with client.audit_logs.export_destinations.with_streaming_response.test(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = response.parse()
            assert_matches_type(AuditLogExportDestinationTestResult, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Kernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.audit_logs.export_destinations.with_raw_response.test(
                "",
            )


class TestAsyncExportDestinations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
            kms_key_id="kms_key_id",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKernel) -> None:
        response = await async_client.audit_logs.export_destinations.with_raw_response.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = await response.parse()
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKernel) -> None:
        async with async_client.audit_logs.export_destinations.with_streaming_response.create(
            bucket="xxx",
            format="jsonl.gz",
            prefix="prefix",
            region="x",
            role_arn="x",
            type="s3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = await response.parse()
            assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.retrieve(
            "id",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKernel) -> None:
        response = await async_client.audit_logs.export_destinations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = await response.parse()
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKernel) -> None:
        async with async_client.audit_logs.export_destinations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = await response.parse()
            assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.audit_logs.export_destinations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.update(
            id="id",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.update(
            id="id",
            bucket="xxx",
            kms_key_id="kms_key_id",
            prefix="prefix",
            region="x",
            role_arn="x",
            status="active",
        )
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKernel) -> None:
        response = await async_client.audit_logs.export_destinations.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = await response.parse()
        assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKernel) -> None:
        async with async_client.audit_logs.export_destinations.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = await response.parse()
            assert_matches_type(AuditLogExportDestination, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.audit_logs.export_destinations.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.list()
        assert_matches_type(AsyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKernel) -> None:
        response = await async_client.audit_logs.export_destinations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = await response.parse()
        assert_matches_type(AsyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKernel) -> None:
        async with async_client.audit_logs.export_destinations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = await response.parse()
            assert_matches_type(AsyncOffsetPagination[AuditLogExportDestination], export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.delete(
            "id",
        )
        assert export_destination is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKernel) -> None:
        response = await async_client.audit_logs.export_destinations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = await response.parse()
        assert export_destination is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKernel) -> None:
        async with async_client.audit_logs.export_destinations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = await response.parse()
            assert export_destination is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.audit_logs.export_destinations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncKernel) -> None:
        export_destination = await async_client.audit_logs.export_destinations.test(
            "id",
        )
        assert_matches_type(AuditLogExportDestinationTestResult, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncKernel) -> None:
        response = await async_client.audit_logs.export_destinations.with_raw_response.test(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_destination = await response.parse()
        assert_matches_type(AuditLogExportDestinationTestResult, export_destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncKernel) -> None:
        async with async_client.audit_logs.export_destinations.with_streaming_response.test(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_destination = await response.parse()
            assert_matches_type(AuditLogExportDestinationTestResult, export_destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncKernel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.audit_logs.export_destinations.with_raw_response.test(
                "",
            )
