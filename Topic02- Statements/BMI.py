#Aaron Donnelly
#This program will calculate the users body mass index (BMI)
a= 18.5
b=25.0

print("This program will calculate you body mass index (BMI)")
weight= float(input("Insert you weight in kg:"))
height= float(input("Insert you height in cm:"))

BMI= weight / (height/100 * height/100)
print("BMI={0:.2f}".format(BMI))
if BMI < a:
        print ("You are underweight")
        
if BMI > b:
        print ("You are overweight")
        
if BMI  >= a and BMI <= b:
        print ("You are a healthy weight")
                   