def calc(weight, height):
    bmi_indx = weight / height ** 2
    return bmi_indx


w = int(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))
bmi = calc(w, h)
print("Your BMI is: ", bmi)
