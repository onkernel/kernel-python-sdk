# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["VaultPaymentMethod", "Capabilities", "CapabilitiesSingleUseCard", "Display"]


class CapabilitiesSingleUseCard(BaseModel):
    eligible: bool

    reasons: List[str]


class Capabilities(BaseModel):
    """Provider-reported advisory capabilities.

    A missing capability is unknown, not ineligible; only eligible=false is an explicit negative signal.
    """

    single_use_card: Optional[CapabilitiesSingleUseCard] = None


class Display(BaseModel):
    brand: Optional[str] = None

    label: Optional[str] = None

    last4: Optional[str] = None


class VaultPaymentMethod(BaseModel):
    id: str

    capabilities: Capabilities
    """Provider-reported advisory capabilities.

    A missing capability is unknown, not ineligible; only eligible=false is an
    explicit negative signal.
    """

    display: Display

    is_default: bool

    provider: str
    """Provider that issued this payment-method ID."""

    type: str
    """Provider-neutral payment-method type normalized to lowercase."""
