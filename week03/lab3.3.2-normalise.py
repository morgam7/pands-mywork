# normalise.py
# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string
# and the normalised one
# Author: Marcella Morgan

rawstring = input ("Enter string: ")
normalised_rawstring = rawstring.strip().lower()

lenght_of_rawstring = len(rawstring)
lenght_of_normalised_rawstring = len(normalised_rawstring)

print (f"That string normalised is: {normalised_rawstring}")
print (f"We reduced the input string from {lenght_of_rawstring} to {lenght_of_normalised_rawstring} characters.")      
       
