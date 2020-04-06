def add():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Sum of a and b is: ", a + b)


add()


def sub(x, y):
    diff = x - y
    print("Difference of x and y is: ", x - y)


sub(20, 10)


def concat(x, y):
    result = x + y
    return result

newstring = concat("Neha", "Sahoo")
print(newstring)


def age(name):
    print(name, "is of age 30")


age(concat("Neha ", "Sahoo"))
