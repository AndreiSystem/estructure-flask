from app.extensions.database import db

_session = db.session

# transformar o atalho criar bando de dados
def init_app(app):
    @app.cli.command()
    def createdb():
        db.create_all()

def save(model: db.Model):
    _session.add(model)
    commit()
    return model

def commit():
    _session.commit()


def delete(model: db.Model) -> None:
    _session.delete(model)

