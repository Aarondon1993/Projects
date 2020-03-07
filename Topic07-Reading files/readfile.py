# Aaron Donnelly
# This program will count the number of re-occurences of the letter 'e' in a txt file selected by the user.

f= open(input("Insert filename  "), "r")
x= f.read().count('e')
print("There are",x, "e's in this text")

