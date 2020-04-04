# Aaron Donnelly
# This program designed to ask the user for a positive integer. The program will then output the values of the calculation that meet the folling criteria.
# If the value is even divide it by 2 but if the value is odd, multiply it by 3 and add 1.

X= int(input(" Please enter a positive integer:"))
print('Integer chosen:',X)
while X!=1:

  if X%2==0:
      X=X/2
      print('X=',X)
  else:
      X = X*3+1
      print('X=',X) 

print ('Thank you for running my program :)')      


