from products_data import retrieve_all_products, retrieve_requested_product
from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

cart_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    all_products = retrieve_all_products()
    return render_template('products.html', products=all_products)

@app.route('/products/<product_id>')
def product(product_id):
    product = retrieve_requested_product(product_id)[0]
    print(product)
    return render_template('product.html', product_details=product)

@app.route('/cart')
def cart():
    total_price = sum([el['Price'] for el in cart_items])
    print(total_price)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/add_product_to_cart/<product_id>')
def add_to_cart(product_id):
    product = retrieve_requested_product(product_id)[0]
    cart_items.append(product)
    return redirect(url_for('cart'))

@app.route('/delete_product_from_cart/<product_id>')
def delete_from_cart(product_id):
    for el in cart_items:
        if el['ProductId'] == product_id:
            cart_items.pop(cart_items.index(el))
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)