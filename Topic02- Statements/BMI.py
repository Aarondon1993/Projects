print("This program will calculate you body mass index (BMI)")
weight= float(input("Insert you weight in kg:"))
height= float(input("Insert you height in cm:"))

BMI= weight / (height/100 * height/100)
print("BMI={0:.2f}".format(BMI))