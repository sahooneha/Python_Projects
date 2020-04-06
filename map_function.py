# map function is use to perform some operation on a list

def square(x):
     return x ** 2


num = [1, 2, 3, 4, 5]

double = list(map(square, num))
print(double)

triple = list(map(lambda x:x**3,num))
print(triple)
