from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from project.database.model import db
    db.init_app(app)

    from project.blueprints.user.routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from project.blueprints.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from project.blueprints.auth.routes import login_manager
    login_manager.init_app(app)
    
    return app

app = create_app('project.config.Config')


