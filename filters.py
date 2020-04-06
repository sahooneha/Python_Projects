numbers = [1, 2, 3, 4, 5, 6, 7]

even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers: ", even_nums)


def odd(x):
    if x % 2 == 1:
        return x


odd_nums = list(filter(odd, numbers))
print("Odd numbers: ", odd_nums)
