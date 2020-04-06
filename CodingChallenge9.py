def stu_discount(x):
    discount1 = x - (0.1 * x)
    return discount1


def add_discount(function, y):
    discount2 = function(y) - (0.05 * function(y))
    return discount2


total_discount = add_discount(stu_discount, 100)
print("total discount --> ", total_discount)


# second way

def student_discount(price):
    price = price - (price * 10) / 100
    return price


def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice


selling_price = 100

# applying both discounts simultaneously

print(additional_discount(student_discount(selling_price)))
