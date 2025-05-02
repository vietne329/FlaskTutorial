from flask import render_template, request
from saleapp import app
import utils

@app.route("/")
def home():
    cates = utils.load_category()
    return render_template('index.html', categories = cates)

@app.route("/products")
def product_list():
    cate_id = request.args.get("category_id")
    keySearch = request.args.get("keySearch")
    from_price = request.args.get("fromPrice")
    to_price = request.args.get("toPrice")

    products = utils.load_products(cate_id= cate_id, keySearch = keySearch, from_price = from_price, to_price = to_price)

    return render_template('products.html', product_list = products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id)
    return render_template('product_detail.html', product = product)


if __name__ == '__main__':
    from saleapp.admin import *

    app.run(debug=True)