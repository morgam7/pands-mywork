# div.py
# program that inputs two number and outputs the integer answer and remainder
# Author: Marcella Morgan

x = int (input ("Enter number: "))
y = int (input ("Enter number you want to divide by: "))
answer = int (x//y)
remainder = x%y
print ("{} divided by {} equals {} with a remainder of {}". format (x,y,answer, remainder))