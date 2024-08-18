from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from project.database.model import db

    db.app = app
    db.init_app(app)

    from project.blueprints.api.routes import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    from project.blueprints.auth.routes import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    from project.blueprints.admin.routes import admin_bp

    app.register_blueprint(admin_bp, url_prefix="/admin")

    from project.blueprints.home.routes import home_bp

    app.register_blueprint(home_bp)

    from project.blueprints.list.routes import list_bp

    app.register_blueprint(list_bp, url_prefix="/list")

    from project.blueprints.auth.routes import login_manager

    login_manager.init_app(app)

    return app


app = create_app("project.config.Config")
