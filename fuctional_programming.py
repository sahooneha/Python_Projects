def add_ten(x):
    return x + 10


def twice(function, arg):
    return function(function(arg))


value = twice(add_ten, 50)
print("value is - {x}".format(x=value))
