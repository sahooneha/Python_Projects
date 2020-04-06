prices = [100, 200, 300, 400]

new_price = list(map(lambda x: x - (0.1 * x), prices))
print(new_price)


# 2nd method

def discount(price):
    price = price - (price * 10) / 100
    return price


product_prices = [100, 200, 300, 400, 500]

updated_prices = list(map(discount, product_prices))

print(updated_prices)
