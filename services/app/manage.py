from project.app import app

from flask.cli import FlaskGroup

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    from project.database import model
    model._create_all()

@cli.command("seed_db")
def seed_db():
    from project.database import model
    model._seed_all()

if __name__ == "__main__":
    cli()