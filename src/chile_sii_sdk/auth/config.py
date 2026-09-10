"""Authentication configuration for SII requests."""

from __future__ import annotations

from dataclasses import dataclass

from chile_sii_sdk.config import SiiConfig


@dataclass(slots=True)
class SiiAuthConfig:
    """Configuration for authentication and signed SII requests."""

    rut: str
    certificate_path: str
    private_key_path: str
    certificate_password: str | None = None
    config: SiiConfig | None = None

    def __post_init__(self) -> None:
        self.rut = self._normalize_rut(self.rut)
        self.config = self.config or SiiConfig()

    @staticmethod
    def _normalize_rut(rut: str) -> str:
        digits = "".join(ch for ch in rut if ch.isdigit())
        if len(digits) < 7:
            raise ValueError("RUT must contain a valid numeric sequence.")
        return digits
