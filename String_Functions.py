mylist = ["1", "2", "3"]
x = "#".join(mylist)
print(x)

#Join works with string only.So in case of an integer list first convert them to string and then join

numlist = [1,2,3]
newlist = [str(i) for i in numlist]
y = "#".join(newlist)
print(y)
print(y.startswith("1"))
print(y.endswith("1"))
z = "Neha"
print(z.lower())
