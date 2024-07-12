from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from project.database.model import db
    db.init_app(app)

    from project.blueprints.user.routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from project.blueprints.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app


app = create_app('project.config.Config')

if __name__ == '__main__':
    app.run(debug=True)
    print(f'HELLO HELLO KEY: {app.config["SECRET_KEY"]}')