from app.extensions.database import db



# transformar o atalho criar bando de dados
def init_app(app):
    @app.cli.command()
    def createdb():
        db.create_all()