from __future__ import annotations

import pytest

from chile_sii_sdk import __version__
from chile_sii_sdk.config import SiiConfig, SiiEnvironment
from chile_sii_sdk.errors import SiiError
from chile_sii_sdk.clients import SyncSiiClient


def test_version_follows_semver() -> None:
    assert __version__ == "0.1.0"


def test_config_defaults_to_certification_environment() -> None:
    config = SiiConfig()
    assert config.environment is SiiEnvironment.CERTIFICATION
    assert config.timeout == 30
    assert config.verify_ssl is True


def test_sync_client_initializes_with_config() -> None:
    config = SiiConfig(environment=SiiEnvironment.PRODUCTION)
    client = SyncSiiClient(config=config)
    assert client.config is config
    assert client.config.environment is SiiEnvironment.PRODUCTION


def test_sii_error_is_raised_for_invalid_environment() -> None:
    with pytest.raises(SiiError, match="Unsupported SII environment"):
        SiiConfig(environment="invalid-environment")
