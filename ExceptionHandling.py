try:
    a=int(input("A: "))
    b=int(input("B: "))
    c=a/b
    print("C: ",c)

except ZeroDivisionError:
    print("Zero Division Error")

finally:
    print("This is going to execute no matter what")