import json, os
from saleapp import app

def read_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def load_category():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))

def load_products(cate_id=None, keySearch=None, from_price=None, to_price=None):
    products = read_json(os.path.join(app.root_path,'data/products.json'))
    if cate_id: #search by category
        products = [p for p in products if p['category_id'] == int(cate_id)]

    if keySearch: #search name products
        products = [p for p in products if p['name'].lower().find(keySearch.lower()) >= 0]

    if from_price:# search by price
        products = [p for p in products if p['price'] >= float(from_price)]

    if to_price:# search by price
        products = [p for p in products if p['price'] <= float(to_price)]
    return products

def get_product_by_id(product_id):
    products = read_json(os.path.join(app.root_path,'data/products.json'))
    for p in products:
        if p['id'] == product_id:
            return p
