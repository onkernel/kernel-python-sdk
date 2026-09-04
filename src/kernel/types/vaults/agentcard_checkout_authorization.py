# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentcardCheckoutAuthorization"]


class AgentcardCheckoutAuthorization(BaseModel):
    """The in-flight or most recent checkout authorization.

    Present while a checkout is pending approval and after it settles.
    """

    id: str

    amount_cents: int

    created_at: datetime

    currency: str

    merchant: str

    psp: str

    status: Literal["awaiting_approval", "approved", "declined", "expired"]

    actual_cents: Optional[int] = None

    amount: Optional[str] = None
    """Display amount shown on the approval screen."""

    amount_authority: Optional[Literal["display_only", "stripe_payment_intent"]] = None

    amount_verified: Optional[bool] = None

    approval_url: Optional[str] = None

    browser_id: Optional[str] = None
    """Browser session that submitted the checkout."""

    charged_amount_cents: Optional[int] = None

    charged_currency: Optional[str] = None

    charged_kind: Optional[Literal["captured", "authorized", "none"]] = None

    expected_cents: Optional[int] = None

    expires_at: Optional[datetime] = None

    psp_error_code: Optional[str] = None

    reason: Optional[str] = None

    replay_attempted: Optional[bool] = None

    replay_delivered: Optional[bool] = None
    """Whether the processor response was delivered to the browser."""

    replay_status: Optional[int] = None
    """HTTP status of the replayed processor response."""
