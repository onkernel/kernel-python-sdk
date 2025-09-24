# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ProxyRetrieveResponse",
    "Config",
    "ConfigDatacenterProxyConfig",
    "ConfigIspProxyConfig",
    "ConfigResidentialProxyConfig",
    "ConfigMobileProxyConfig",
    "ConfigCustomProxyConfig",
]


class ConfigDatacenterProxyConfig(BaseModel):
    country: str
    """ISO 3166 country code or EU for the proxy exit node."""


class ConfigIspProxyConfig(BaseModel):
    country: str
    """ISO 3166 country code or EU for the proxy exit node."""


class ConfigResidentialProxyConfig(BaseModel):
    asn: Optional[str] = None
    """Autonomous system number. See https://bgp.potaroo.net/cidr/autnums.html"""

    city: Optional[str] = None
    """City name (no spaces, e.g.

    `sanfrancisco`). If provided, `country` must also be provided.
    """

    country: Optional[str] = None
    """ISO 3166 country code or EU for the proxy exit node.

    Required if `city` is provided.
    """

    os: Optional[Literal["windows", "macos", "android"]] = None
    """Operating system of the residential device."""

    state: Optional[str] = None
    """Two-letter state code."""

    zip: Optional[str] = None
    """US ZIP code."""


class ConfigMobileProxyConfig(BaseModel):
    asn: Optional[str] = None
    """Autonomous system number. See https://bgp.potaroo.net/cidr/autnums.html"""

    carrier: Optional[
        Literal[
            "a1",
            "aircel",
            "airtel",
            "att",
            "celcom",
            "chinamobile",
            "claro",
            "comcast",
            "cox",
            "digi",
            "dt",
            "docomo",
            "dtac",
            "etisalat",
            "idea",
            "kyivstar",
            "meo",
            "megafon",
            "mtn",
            "mtnza",
            "mts",
            "optus",
            "orange",
            "qwest",
            "reliance_jio",
            "robi",
            "sprint",
            "telefonica",
            "telstra",
            "tmobile",
            "tigo",
            "tim",
            "verizon",
            "vimpelcom",
            "vodacomza",
            "vodafone",
            "vivo",
            "zain",
            "vivabo",
            "telenormyanmar",
            "kcelljsc",
            "swisscom",
            "singtel",
            "asiacell",
            "windit",
            "cellc",
            "ooredoo",
            "drei",
            "umobile",
            "cableone",
            "proximus",
            "tele2",
            "mobitel",
            "o2",
            "bouygues",
            "free",
            "sfr",
            "digicel",
        ]
    ] = None
    """Mobile carrier."""

    city: Optional[str] = None
    """City name (no spaces, e.g.

    `sanfrancisco`). If provided, `country` must also be provided.
    """

    country: Optional[str] = None
    """ISO 3166 country code or EU for the proxy exit node.

    Required if `city` is provided.
    """

    state: Optional[str] = None
    """Two-letter state code."""

    zip: Optional[str] = None
    """US ZIP code."""


class ConfigCustomProxyConfig(BaseModel):
    host: str
    """Proxy host address or IP."""

    port: int
    """Proxy port."""

    has_password: Optional[bool] = None
    """Whether the proxy has a password."""

    username: Optional[str] = None
    """Username for proxy authentication."""


Config: TypeAlias = Union[
    ConfigDatacenterProxyConfig,
    ConfigIspProxyConfig,
    ConfigResidentialProxyConfig,
    ConfigMobileProxyConfig,
    ConfigCustomProxyConfig,
]


class ProxyRetrieveResponse(BaseModel):
    type: Literal["datacenter", "isp", "residential", "mobile", "custom"]
    """Proxy type to use.

    In terms of quality for avoiding bot-detection, from best to worst: `mobile` >
    `residential` > `isp` > `datacenter`.
    """

    id: Optional[str] = None

    config: Optional[Config] = None
    """Configuration specific to the selected proxy `type`."""

    name: Optional[str] = None
    """Readable name of the proxy."""
