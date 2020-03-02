from importlib import import_module
from dynaconf import FlaskDynaconf

# Gerencia as Configurações
def init_app(app):
    FlaskDynaconf(app)