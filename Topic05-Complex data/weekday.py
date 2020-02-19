# Aaron Donnelly
# This program is designed to determine if today is a weekday or weekend day.

import datetime

# This will import the datetime module
now = datetime.datetime.now()
# This allows me to print the current date
if now.weekday()== 0 or 1 or 2 or 3 or 4:
#This allows me to determine which day it is based on the datetime
# 0 = Monday, 1= Tuesday... and so on
 print('Unfortuntely today is a weekday')
#if the value for now.weekday() is not 0-4 it is the weekend
else:
    print(' Yayyyyyy its the weekend')


