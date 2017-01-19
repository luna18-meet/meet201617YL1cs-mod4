#This module tests the my_str method
from my_str import MyStr

#Make a new MyStr instance
my_string=MyStr('Hello world')

#Print the original string
print(my_string)

#Test the exclaim method (given to you)
print(my_string.exclaim(20))

#Test the new replace method
print(my_string.replace('h','j'))

#Test the new replace method
my_string=MyStr('aAaADD')
print(my_string.replace('AA','c'))

