# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PlaywrightExecuteParams"]


class PlaywrightExecuteParams(TypedDict, total=False):
    code: Required[str]
    """TypeScript/JavaScript code to execute.

    The code has access to 'page', 'context', and 'browser' variables. It runs
    within a function, so you can use a return statement at the end to return a
    value. This value is returned as the `result` property in the response. Example:
    "await page.goto('https://example.com'); return await page.title();"
    """

    timeout_sec: int
    """Maximum execution time in seconds. Default is 60."""
