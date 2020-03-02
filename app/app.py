from flask import Flask
from app.extensions import configuration
from app.extensions import commands
from app.extensions import database
from app.extensions import admin
from app.extensions import appearance
from app.extensions import auth
from app.blueprints import views
from app.blueprints import restapi

# Start app
app = Flask(__name__)

configuration.init_app(app)
commands.init_app(app)
database.init_app(app)
admin.init_app(app)
appearance.init_app(app)
auth.init_app(app)
views.init_app(app)
restapi.init_app(app)

