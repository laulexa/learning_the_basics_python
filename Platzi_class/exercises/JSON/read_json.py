import json

with open('products.json', mode='r') as file:
    products = json.load(file)

#Show the content
for product in products:
    #print(product)
    print(f"product: {product['name']}, Price: {product['price']}")