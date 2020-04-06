list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c"]
print(list1 + list2)
print(list1 * 2)
if 1 in list1:
    print ("a is in list2")
else:
    print("Not in list2")
list3 = ["apple", "orange", "kiwi"]
print("Length of list3",len(list3))
list3.append("litchi")
print("List3 after adding litchi",list3)
list3.insert(1,"banana")
print("List3 after adding banana",list3)

list4 = list((7,8,9))
print(list4)