"""Asynchronous client interface for the Chile SII SDK."""

from __future__ import annotations


class AsyncSiiClient:
    """Async client scaffold for the v0.2.0 authentication milestone."""

    def ping(self) -> str:
        """Return the client readiness status."""
        return "SII async client ready"
