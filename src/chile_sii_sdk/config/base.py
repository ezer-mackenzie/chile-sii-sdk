"""Environment and client configuration."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from chile_sii_sdk.errors import SiiError


class SiiEnvironment(str, Enum):
    """Supported SII operating environments."""

    CERTIFICATION = "certification"
    PRODUCTION = "production"


@dataclass(slots=True)
class SiiConfig:
    """Configuration for SII API access."""

    environment: SiiEnvironment | str = SiiEnvironment.CERTIFICATION
    timeout: int = 30
    verify_ssl: bool = True
    certificate_path: str | None = None
    private_key_path: str | None = None
    certificate_password: str | None = None

    def __post_init__(self) -> None:
        if isinstance(self.environment, str):
            try:
                self.environment = SiiEnvironment(self.environment)
            except ValueError as exc:
                raise SiiError(
                    "Unsupported SII environment. Use 'certification' or 'production'."
                ) from exc

        if self.timeout <= 0:
            raise SiiError("SII timeout must be greater than zero.")
