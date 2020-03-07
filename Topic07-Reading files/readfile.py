# Aaron Donnelly
# This program will count the number of re-occurences of the letter 'e' in a txt file titled moby-dick.py
f= open("moby-dick.txt", "r")
x= f.read().count('e')
print(x)

