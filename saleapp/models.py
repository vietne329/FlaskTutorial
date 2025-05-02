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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Kiểm tra xem đã có dữ liệu category chưa
        if Category.query.count() == 0:
            c1 = Category(name='Phone')
            c2 = Category(name='Tablet')
            c3 = Category(name='Smart watch')
            db.session.add_all([c1, c2, c3])
            db.session.commit()
            print("Categories added")
        else:
            print("Categories already exist")