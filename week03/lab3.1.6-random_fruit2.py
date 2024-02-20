# random fruit
# Program that outputs a random fruit
# author Marcella Morgan

import random

fruits = ("Apple", "Orange", "Pear", "Banana")
index = random.randint (0, len(fruits)-1)
fruit = fruits [index]
print ("A random fruit: {}" . format (fruit))