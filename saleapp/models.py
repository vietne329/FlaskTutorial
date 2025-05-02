from unicodedata import category

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import app,db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True     # không tại bảng BaseModel
    id = Column(Integer, primary_key=True, autoincrement= True)

class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    __tablename__ = 'product'
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


# with app.app_context():
#     # db.create_all()
#     c1 = Category(name='Phone')
#     c2 = Category(name='Tablet')
#     c3 = Category(name='Smart watch')
#     db.session.add(c1)
#     db.session.add(c2)
#     db.session.add(c3)
#     db.session.commit()
#
#     products = [{
#         "id": 1,
#         "name": "Iphone 7 Plus",
#         "description": "Apple, 32GB, RAM:3GB, iOS13",
#         "price": 17000000,
#         "image": "images/i7pls.webp",
#         "category_id": 1
#     },{
#         "id": 2,
#         "name": "Ipad Pro 2020",
#         "description": "Apple, 128GB, RAM:6GB, iOS13",
#         "price": 32000000,
#         "image": "images/i7pls.webp",
#         "category_id": 2
#     },{
#         "id": 3,
#         "name": "Galaxy Note 10 Plus",
#         "description": "Samsung, 64GB, RAM:6GB",
#         "price": 24000000,
#         "image": "images/i7pls.webp",
#         "category_id": 1
#     }]
#
#     for p in products:
#         pro = Product(name = p['name'], description = p['description'], price = p['price'], image = p['image'] ,category_id = p['category_id'])
#         db.session.add(pro)
#
#     db.session.commit()
#
#     print("Tables created")