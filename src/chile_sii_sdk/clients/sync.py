"""Synchronous client interface for the Chile SII SDK."""

from __future__ import annotations

from chile_sii_sdk.config import SiiConfig


class SyncSiiClient:
    """A synchronous client that exposes the initial project contract."""

    def __init__(self, config: SiiConfig | None = None) -> None:
        self.config = config or SiiConfig()

    def ping(self) -> str:
        """Placeholder method to verify the client is active."""
        return f"SII client ready in {self.config.environment.value} mode"
