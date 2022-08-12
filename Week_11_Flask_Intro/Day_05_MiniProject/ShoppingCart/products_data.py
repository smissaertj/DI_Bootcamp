import json

def retrieve_all_products():
    with open('products.json', 'r') as file:
        all_products = json.load(file)
    return all_products


def retrieve_requested_product(product_id):
    requested_product =  [el for el in retrieve_all_products() if el['ProductId'] == product_id]
    return requested_product


