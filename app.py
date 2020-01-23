from dynaconf import FlaskDynaconf
from flask import Flask, abort, render_template
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_bootstrap import Bootstrap
from flask_simplelogin import SimpleLogin, login_required
from flask_sqlalchemy import SQLAlchemy

# Start app
app = Flask(__name__)

# Gerencia as Configurações
FlaskDynaconf(app)

# Banco de dados
db = SQLAlchemy(app)

def verify_login(user):
    return user.get("username") == "addmin" and user.get('password') == '123'

SimpleLogin(app, login_checker=verify_login)

# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin(app, name=app.config.TITLE, template_mode='bootstrap3')

# Model
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)

# iniciando admin
admin.add_view(sqla.ModelView(Products, db.session))

# transformar o atalho criar bando de dados
@app.cli.command()
def createdb():
    # Criando sqlite database
    db.create_all()

# Views
@app.route('/')
def index():
    products = Products.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<product_id>')
def product(product_id):
    product = Products.query.filter_by(id=product_id).first() or abort( 404, 'produto não encontrado')

    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
