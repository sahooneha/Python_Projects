def even_num():
    for i in range(21):
        if i % 2 == 0:
            yield i


even_list = list(even_num())
print("List - ", even_list)
