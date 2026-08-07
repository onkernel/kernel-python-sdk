# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "AuthContext",
    "Authentication",
    "Authorization",
    "AuthorizationCredentialScope",
    "AuthorizationEffectiveScope",
    "Organization",
    "Principal",
]


class Authentication(BaseModel):
    credential_id: Optional[str] = None
    """
    The API key ID when authenticated with an API key; null for session credentials.
    """

    method: Literal["api_key", "jwt"]
    """The credential format used to authenticate the request."""

    source: Literal["api_key", "oauth", "dashboard"]
    """The source classification resolved by authentication middleware."""


class AuthorizationCredentialScope(BaseModel):
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """

    project_id: Optional[str] = None
    """The Kernel project ID, or null when the scope is organization-wide."""


class AuthorizationEffectiveScope(BaseModel):
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """

    project_id: Optional[str] = None
    """The Kernel project ID, or null when the scope is organization-wide."""


class Authorization(BaseModel):
    """The credential's maximum scope and the effective scope selected for this request.

    Future permission data can be added without changing scope semantics.
    """

    credential_scope: AuthorizationCredentialScope
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """

    effective_scope: AuthorizationEffectiveScope
    """A scope within the authenticated organization.

    A null project_id represents organization-wide scope.
    """


class Organization(BaseModel):
    id: str
    """The authenticated Kernel organization ID."""


class Principal(BaseModel):
    id: str
    """The API key ID for API-key principals or user ID for user principals."""

    type: Literal["api_key", "user"]
    """The kind of principal authenticated for the request."""


class AuthContext(BaseModel):
    """The identity and authorization context resolved for the current request."""

    authentication: Authentication

    authorization: Authorization
    """The credential's maximum scope and the effective scope selected for this
    request.

    Future permission data can be added without changing scope semantics.
    """

    organization: Organization

    principal: Principal
