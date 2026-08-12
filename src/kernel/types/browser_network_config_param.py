# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["BrowserNetworkConfigParam"]


class BrowserNetworkConfigParam(TypedDict, total=False):
    """Network configuration for a browser session or browser pool."""

    private_hosts: SequenceNotStr[str]
    """
    Destinations the browser reaches directly through the session's own network
    instead of through Kernel-managed egress — for private hosts reachable over a
    VPN or tunnel the session has joined (e.g. a Tailscale tailnet). By default,
    private IP ranges already route directly: RFC1918 (10.0.0.0/8, 172.16.0.0/12,
    192.168.0.0/16), CGNAT/Tailscale (100.64.0.0/10), and IPv6 ULA (fc00::/7). An
    explicitly supplied list replaces those defaults with exactly the entries given,
    and an empty list ([]) disables them so all traffic uses Kernel-managed egress;
    omit private_hosts to keep the defaults. Entries are hostname patterns
    ("_.example.ts.net", "preview.internal") or IP/CIDR literals ("100.64.0.0/10",
    "10.1.30.63"). IP and CIDR entries only match URLs written with a literal IP
    address; they never match hostnames that resolve into the range, so private DNS
    names need a hostname entry even when they resolve inside the default ranges.
    CIDRs must be in canonical masked form (host bits zero), and only the private
    ranges listed above are accepted; public, loopback, link-local, and unspecified
    ranges are rejected. Exact IPv6 addresses must be bracketed ("[fd00::1]"); IPv6
    CIDR ranges are unbracketed ("fd00::/8"). Wildcards are limited to one leading
    "_." over a suffix with at least two labels that is not a public suffix (so
    "_.co.uk" or "_.ts.net" are rejected, while "\\**.example.ts.net" is accepted).
    Hostname and IP entries may carry a port; CIDR ranges may not. Hostname entries
    are not resolved during validation, so callers must ensure they identify private
    destinations. Not related to a proxy's bypass_hosts, which selects between
    upstream-proxy and Kernel-managed direct egress and cannot reach into a VPN.
    """
