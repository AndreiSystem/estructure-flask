from flask import Flask
from app.extensions import configuration

# Start app
app = Flask(__name__)

configuration.load_extensions(app)

