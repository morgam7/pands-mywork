# message = 'I have eaten ' + 99 + ' burritos.'
# print (message)

# The issue is that it is reading 99 as a string. It needs to be an integer or to have a brackets around it.

message = 'I have eaten ' + int (99) + ' burritos.'
print (message)