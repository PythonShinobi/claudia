import os

from app import create_app
from app.config import (
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
)


configurations = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}

environment = os.environ.get("APP_ENV", "development").lower()

config_class = configurations.get(environment)

if config_class is None:
    raise ValueError(
        f"Unknown application environment: {environment}"
    )

app = create_app(config_class)


if __name__ == "__main__":
    app.run()