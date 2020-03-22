# Aaron Donnelly
# Calculating the approximate square root of a float number.

def square_root(y):
    return(g)
Percision= 0.001
Y= float(input("Please input the number you want the square root of:"))
g= Y/2.0

while abs(g*g-Y)>= Percision:
    g= g-(((g**2)-Y)/(2*g))
print (" Square root of ", Y, "is approximately", g)