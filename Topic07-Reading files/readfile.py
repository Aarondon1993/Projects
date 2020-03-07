# Aaron Donnelly
# This program will count the number of re=occurences of the letter 'e' in a txt file
f= open("moby-dick.txt", "r")
x= f.read().count('e')
print(x)