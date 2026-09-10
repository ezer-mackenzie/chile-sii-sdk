"""Token model for SII authenticated sessions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SiiToken:
    """Represents an access token returned by the SII authentication flow."""

    token: str
    seed: str
    rut: str
    expires_at: str | None = None
