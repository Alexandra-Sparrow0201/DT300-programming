#-------------------------------------------------------------------------------
# Name:        t_re
# Purpose: testing of regular expressions
#
# Author:      halla
#
# Created:     09/04/2018
import re

fileName = input("Here")
validate = True
if re.match("^[a-zA-Z0-9_]+$", fileName): #Checking that there is only letters, numbers, and undersocores
    print("Only alphabetical letters and spaces: yes") #For testing purposes DELETE LATER
    validate = True
else:
    print("Please only use letters of the alphabet or numbers for file name. No special characters except undersorces.")
    validate = False

print (validate)