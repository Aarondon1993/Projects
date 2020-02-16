# Aaron Donnelly
# This program will read a students grade
# and print out the corresponding grade.

percentage = float(input("Please input the percentage:"))
if percentage < 40:
 print ("Fail")
elif percentage < 50:
 print("Pass") 
elif percentage < 60:
 print("Merit 1")
elif percentage < 70:
 print("Merit 2")
else:
 print("Distinction")  
