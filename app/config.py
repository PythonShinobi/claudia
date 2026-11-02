import os


class BaseConfig:
    """Settings shared by all environments."""

    SECRET_KEY = os.environ.get("SECRET_KEY")
    WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER", "")

    TESTING = False
    DEBUG = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


class DevelopmentConfig(BaseConfig):
    """Settings for local development."""
    ENVIRONMENT = "development"

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-only-change-me"
    )

    DEBUG = True


class TestingConfig(BaseConfig):
    """Settings for automated tests."""

    ENVIRONMENT = "testing"

    SECRET_KEY = "test-secret-key"
    WHATSAPP_NUMBER = "254700000000"

    TESTING = True


class ProductionConfig(BaseConfig):
    """Settings for the live website."""

    ENVIRONMENT = "production"

    DEBUG = False
    SESSION_COOKIE_SECURE = True