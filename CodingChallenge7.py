product_details = {"mobile": 85000,
                   "tv": 105000,
                   "fridge": 35000,
                   "washing machine": 40000}
product = input("Enter a product name:")
if product in product_details:
    print("Price of the {x} is {y}".format(x=product, y=product_details[product]))
else:
    print("Invalid product name")
