people = {"Neha": 30, "Swapna": 33}
print(people)
print(people["Neha"])
print(people.get("Ricky"))
print(people.get("Ricky","No keyword"))

print("Ricky" in people)

for i in people:
    print(people[i])
    print(i)

print("Length of people ",len(people))
print("Printable string representation of dict",str(people))
print("Type of people ",type(people))


