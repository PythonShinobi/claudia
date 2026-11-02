from flask import Flask, render_template

from app.config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)

    # Load application configuration.
    app.config.from_object(config_class)

    # Production must have a secret key supplied through the environment.
    if (
        config_class.__name__ == "ProductionConfig"
        and not app.config.get("SECRET_KEY")
    ):
        raise RuntimeError(
            "SECRET_KEY must be configured in production."
        )

    # Register application blueprints
    from app.main import main_blueprint
    app.register_blueprint(main_blueprint)    

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.html"), 500

    return app

