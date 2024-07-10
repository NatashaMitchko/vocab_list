from flask.cli import FlaskGroup

from project.app import app
from project.database import model

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    model._create_all()

if __name__ == "__main__":
    cli()