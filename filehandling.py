file = open("Demo.txt", "w")
for i in range(10):
    file.write(str(i))
    file.write("\n")

file.close()

file = open("Demo.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()


