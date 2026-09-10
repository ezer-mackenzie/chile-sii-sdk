from __future__ import annotations

from chile_sii_sdk import __version__
from chile_sii_sdk.auth import SiiAuthConfig, SiiAuthSession
from chile_sii_sdk.clients import AsyncSiiClient, SyncSiiClient


def test_version_is_v020() -> None:
    assert __version__ == "0.2.0"


def test_auth_config_requires_certificate_paths() -> None:
    config = SiiAuthConfig(
        rut="18.123.456-5",
        certificate_path="/tmp/cert.p12",
        private_key_path="/tmp/key.pem",
        certificate_password="secret",
    )

    assert config.rut == "181234565"
    assert config.certificate_path == "/tmp/cert.p12"
    assert config.private_key_path == "/tmp/key.pem"
    assert config.certificate_password == "secret"


def test_auth_session_generates_seed_and_token() -> None:
    auth = SiiAuthSession(
        config=SiiAuthConfig(
            rut="18.123.456-5",
            certificate_path="/tmp/cert.p12",
            private_key_path="/tmp/key.pem",
            certificate_password="secret",
        )
    )

    seed = auth.generate_seed()
    token = auth.issue_token(seed=seed)

    assert seed
    assert token.token
    assert token.seed == seed
    assert token.rut == "181234565"


def test_async_client_can_be_instantiated() -> None:
    client = AsyncSiiClient()
    assert client.ping() == "SII async client ready"


def test_sync_client_auth_method_uses_session() -> None:
    client = SyncSiiClient()
    session = client.get_auth_session(
        rut="18.123.456-5",
        certificate_path="/tmp/cert.p12",
        private_key_path="/tmp/key.pem",
        certificate_password="secret",
    )

    assert session.config.rut == "181234565"
    assert session.generate_seed()
