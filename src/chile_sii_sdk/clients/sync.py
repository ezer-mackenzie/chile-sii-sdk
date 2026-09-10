"""Synchronous client interface for the Chile SII SDK."""

from __future__ import annotations

from chile_sii_sdk.auth import SiiAuthConfig, SiiAuthSession
from chile_sii_sdk.config import SiiConfig


class SyncSiiClient:
    """A synchronous client that exposes the initial project contract."""

    def __init__(self, config: SiiConfig | None = None) -> None:
        self.config = config or SiiConfig()

    def ping(self) -> str:
        """Placeholder method to verify the client is active."""
        env = self.config.normalized_environment
        return f"SII client ready in {env.value} mode"

    def get_auth_session(
        self,
        rut: str,
        certificate_path: str,
        private_key_path: str,
        certificate_password: str | None = None,
    ) -> SiiAuthSession:
        """Create an authenticated SII session for the caller."""
        auth_config = SiiAuthConfig(
            rut=rut,
            certificate_path=certificate_path,
            private_key_path=private_key_path,
            certificate_password=certificate_password,
            config=self.config,
        )
        return SiiAuthSession(config=auth_config)
