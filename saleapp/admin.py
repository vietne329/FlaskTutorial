from saleapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Product

admin = Admin(app=app, name= "E-commerce Administration", template_mode='bootstrap4')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))

