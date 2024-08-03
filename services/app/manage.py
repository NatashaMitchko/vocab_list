from project.app import app

from flask.cli import FlaskGroup

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    from project.database import seed
    seed._create_all()

@cli.command("seed_db")
def seed_db():
    from project.database import seed
    seed._seed_all()

@cli.command("list_routes")
def list_routes():
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.urlparse("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == "__main__":
    cli()