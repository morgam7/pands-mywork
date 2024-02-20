# random number generator
# prints out a random number
# Author: Marcella Morgan

import random
number = random.randint (1,10)
print ("Here is a random number: {}". format (number))

x = int (input ("Now you choose the range! Enter the smallest number: "))
y = int (input ("Now enter the biggest number: "))
number = random.randint (x,y)
print ("Here is your random number: {}". format (number))
