"""Authentication flow helpers for the Chile SII SDK."""

from __future__ import annotations

from uuid import uuid4

from .config import SiiAuthConfig
from .token import SiiToken


class SiiAuthSession:
    """Represents an authenticated SII session context."""

    def __init__(self, config: SiiAuthConfig) -> None:
        self.config = config

    def generate_seed(self) -> str:
        """Generate a random seed string for the SII auth flow."""
        return uuid4().hex

    def issue_token(self, seed: str) -> SiiToken:
        """Build a token value for the session using the supplied seed."""
        token_value = f"token-{seed}-{self.config.rut}"
        return SiiToken(
            token=token_value,
            seed=seed,
            rut=self.config.rut,
            expires_at=None,
        )
