# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .watch import (
    WatchResource,
    AsyncWatchResource,
    WatchResourceWithRawResponse,
    AsyncWatchResourceWithRawResponse,
    WatchResourceWithStreamingResponse,
    AsyncWatchResourceWithStreamingResponse,
)
from ...._files import read_file_content, async_read_file_content
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileContent
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.browsers import (
    f_move_params,
    f_file_info_params,
    f_read_file_params,
    f_list_files_params,
    f_write_file_params,
    f_delete_file_params,
    f_create_directory_params,
    f_delete_directory_params,
    f_set_file_permissions_params,
)
from ....types.browsers.f_file_info_response import FFileInfoResponse
from ....types.browsers.f_list_files_response import FListFilesResponse

__all__ = ["FsResource", "AsyncFsResource"]


class FsResource(SyncAPIResource):
    @cached_property
    def watch(self) -> WatchResource:
        return WatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> FsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return FsResourceWithStreamingResponse(self)

    def create_directory(
        self,
        id: str,
        *,
        path: str,
        mode: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a new directory

        Args:
          path: Absolute directory path to create.

          mode: Optional directory mode (octal string, e.g. 755). Defaults to 755.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/browsers/{id}/fs/create_directory",
            body=maybe_transform(
                {
                    "path": path,
                    "mode": mode,
                },
                f_create_directory_params.FCreateDirectoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_directory(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a directory

        Args:
          path: Absolute path to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/browsers/{id}/fs/delete_directory",
            body=maybe_transform({"path": path}, f_delete_directory_params.FDeleteDirectoryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_file(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a file

        Args:
          path: Absolute path to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/browsers/{id}/fs/delete_file",
            body=maybe_transform({"path": path}, f_delete_file_params.FDeleteFileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def file_info(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FFileInfoResponse:
        """
        Get information about a file or directory

        Args:
          path: Absolute path of the file or directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/browsers/{id}/fs/file_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"path": path}, f_file_info_params.FFileInfoParams),
            ),
            cast_to=FFileInfoResponse,
        )

    def list_files(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FListFilesResponse:
        """
        List files in a directory

        Args:
          path: Absolute directory path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/browsers/{id}/fs/list_files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"path": path}, f_list_files_params.FListFilesParams),
            ),
            cast_to=FListFilesResponse,
        )

    def move(
        self,
        id: str,
        *,
        dest_path: str,
        src_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Move or rename a file or directory

        Args:
          dest_path: Absolute destination path.

          src_path: Absolute source path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/browsers/{id}/fs/move",
            body=maybe_transform(
                {
                    "dest_path": dest_path,
                    "src_path": src_path,
                },
                f_move_params.FMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read_file(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Read file contents

        Args:
          path: Absolute file path to read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/browsers/{id}/fs/read_file",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"path": path}, f_read_file_params.FReadFileParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def set_file_permissions(
        self,
        id: str,
        *,
        mode: str,
        path: str,
        group: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Set file or directory permissions/ownership

        Args:
          mode: File mode bits (octal string, e.g. 644).

          path: Absolute path whose permissions are to be changed.

          group: New group name or GID.

          owner: New owner username or UID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/browsers/{id}/fs/set_file_permissions",
            body=maybe_transform(
                {
                    "mode": mode,
                    "path": path,
                    "group": group,
                    "owner": owner,
                },
                f_set_file_permissions_params.FSetFilePermissionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def write_file(
        self,
        id: str,
        contents: FileContent,
        *,
        path: str,
        mode: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Write or create a file

        Args:
          path: Destination absolute file path.

          mode: Optional file mode (octal string, e.g. 644). Defaults to 644.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return self._put(
            f"/browsers/{id}/fs/write_file",
            body=read_file_content(contents),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "mode": mode,
                    },
                    f_write_file_params.FWriteFileParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncFsResource(AsyncAPIResource):
    @cached_property
    def watch(self) -> AsyncWatchResource:
        return AsyncWatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onkernel/kernel-python-sdk#with_streaming_response
        """
        return AsyncFsResourceWithStreamingResponse(self)

    async def create_directory(
        self,
        id: str,
        *,
        path: str,
        mode: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a new directory

        Args:
          path: Absolute directory path to create.

          mode: Optional directory mode (octal string, e.g. 755). Defaults to 755.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/browsers/{id}/fs/create_directory",
            body=await async_maybe_transform(
                {
                    "path": path,
                    "mode": mode,
                },
                f_create_directory_params.FCreateDirectoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_directory(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a directory

        Args:
          path: Absolute path to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/browsers/{id}/fs/delete_directory",
            body=await async_maybe_transform({"path": path}, f_delete_directory_params.FDeleteDirectoryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_file(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a file

        Args:
          path: Absolute path to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/browsers/{id}/fs/delete_file",
            body=await async_maybe_transform({"path": path}, f_delete_file_params.FDeleteFileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def file_info(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FFileInfoResponse:
        """
        Get information about a file or directory

        Args:
          path: Absolute path of the file or directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/browsers/{id}/fs/file_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"path": path}, f_file_info_params.FFileInfoParams),
            ),
            cast_to=FFileInfoResponse,
        )

    async def list_files(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FListFilesResponse:
        """
        List files in a directory

        Args:
          path: Absolute directory path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/browsers/{id}/fs/list_files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"path": path}, f_list_files_params.FListFilesParams),
            ),
            cast_to=FListFilesResponse,
        )

    async def move(
        self,
        id: str,
        *,
        dest_path: str,
        src_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Move or rename a file or directory

        Args:
          dest_path: Absolute destination path.

          src_path: Absolute source path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/browsers/{id}/fs/move",
            body=await async_maybe_transform(
                {
                    "dest_path": dest_path,
                    "src_path": src_path,
                },
                f_move_params.FMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read_file(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Read file contents

        Args:
          path: Absolute file path to read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/browsers/{id}/fs/read_file",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"path": path}, f_read_file_params.FReadFileParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def set_file_permissions(
        self,
        id: str,
        *,
        mode: str,
        path: str,
        group: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Set file or directory permissions/ownership

        Args:
          mode: File mode bits (octal string, e.g. 644).

          path: Absolute path whose permissions are to be changed.

          group: New group name or GID.

          owner: New owner username or UID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/browsers/{id}/fs/set_file_permissions",
            body=await async_maybe_transform(
                {
                    "mode": mode,
                    "path": path,
                    "group": group,
                    "owner": owner,
                },
                f_set_file_permissions_params.FSetFilePermissionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def write_file(
        self,
        id: str,
        contents: FileContent,
        *,
        path: str,
        mode: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Write or create a file

        Args:
          path: Destination absolute file path.

          mode: Optional file mode (octal string, e.g. 644). Defaults to 644.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return await self._put(
            f"/browsers/{id}/fs/write_file",
            body=await async_read_file_content(contents),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "mode": mode,
                    },
                    f_write_file_params.FWriteFileParams,
                ),
            ),
            cast_to=NoneType,
        )


class FsResourceWithRawResponse:
    def __init__(self, fs: FsResource) -> None:
        self._fs = fs

        self.create_directory = to_raw_response_wrapper(
            fs.create_directory,
        )
        self.delete_directory = to_raw_response_wrapper(
            fs.delete_directory,
        )
        self.delete_file = to_raw_response_wrapper(
            fs.delete_file,
        )
        self.file_info = to_raw_response_wrapper(
            fs.file_info,
        )
        self.list_files = to_raw_response_wrapper(
            fs.list_files,
        )
        self.move = to_raw_response_wrapper(
            fs.move,
        )
        self.read_file = to_custom_raw_response_wrapper(
            fs.read_file,
            BinaryAPIResponse,
        )
        self.set_file_permissions = to_raw_response_wrapper(
            fs.set_file_permissions,
        )
        self.write_file = to_raw_response_wrapper(
            fs.write_file,
        )

    @cached_property
    def watch(self) -> WatchResourceWithRawResponse:
        return WatchResourceWithRawResponse(self._fs.watch)


class AsyncFsResourceWithRawResponse:
    def __init__(self, fs: AsyncFsResource) -> None:
        self._fs = fs

        self.create_directory = async_to_raw_response_wrapper(
            fs.create_directory,
        )
        self.delete_directory = async_to_raw_response_wrapper(
            fs.delete_directory,
        )
        self.delete_file = async_to_raw_response_wrapper(
            fs.delete_file,
        )
        self.file_info = async_to_raw_response_wrapper(
            fs.file_info,
        )
        self.list_files = async_to_raw_response_wrapper(
            fs.list_files,
        )
        self.move = async_to_raw_response_wrapper(
            fs.move,
        )
        self.read_file = async_to_custom_raw_response_wrapper(
            fs.read_file,
            AsyncBinaryAPIResponse,
        )
        self.set_file_permissions = async_to_raw_response_wrapper(
            fs.set_file_permissions,
        )
        self.write_file = async_to_raw_response_wrapper(
            fs.write_file,
        )

    @cached_property
    def watch(self) -> AsyncWatchResourceWithRawResponse:
        return AsyncWatchResourceWithRawResponse(self._fs.watch)


class FsResourceWithStreamingResponse:
    def __init__(self, fs: FsResource) -> None:
        self._fs = fs

        self.create_directory = to_streamed_response_wrapper(
            fs.create_directory,
        )
        self.delete_directory = to_streamed_response_wrapper(
            fs.delete_directory,
        )
        self.delete_file = to_streamed_response_wrapper(
            fs.delete_file,
        )
        self.file_info = to_streamed_response_wrapper(
            fs.file_info,
        )
        self.list_files = to_streamed_response_wrapper(
            fs.list_files,
        )
        self.move = to_streamed_response_wrapper(
            fs.move,
        )
        self.read_file = to_custom_streamed_response_wrapper(
            fs.read_file,
            StreamedBinaryAPIResponse,
        )
        self.set_file_permissions = to_streamed_response_wrapper(
            fs.set_file_permissions,
        )
        self.write_file = to_streamed_response_wrapper(
            fs.write_file,
        )

    @cached_property
    def watch(self) -> WatchResourceWithStreamingResponse:
        return WatchResourceWithStreamingResponse(self._fs.watch)


class AsyncFsResourceWithStreamingResponse:
    def __init__(self, fs: AsyncFsResource) -> None:
        self._fs = fs

        self.create_directory = async_to_streamed_response_wrapper(
            fs.create_directory,
        )
        self.delete_directory = async_to_streamed_response_wrapper(
            fs.delete_directory,
        )
        self.delete_file = async_to_streamed_response_wrapper(
            fs.delete_file,
        )
        self.file_info = async_to_streamed_response_wrapper(
            fs.file_info,
        )
        self.list_files = async_to_streamed_response_wrapper(
            fs.list_files,
        )
        self.move = async_to_streamed_response_wrapper(
            fs.move,
        )
        self.read_file = async_to_custom_streamed_response_wrapper(
            fs.read_file,
            AsyncStreamedBinaryAPIResponse,
        )
        self.set_file_permissions = async_to_streamed_response_wrapper(
            fs.set_file_permissions,
        )
        self.write_file = async_to_streamed_response_wrapper(
            fs.write_file,
        )

    @cached_property
    def watch(self) -> AsyncWatchResourceWithStreamingResponse:
        return AsyncWatchResourceWithStreamingResponse(self._fs.watch)
