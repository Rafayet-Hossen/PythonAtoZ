#Errors & exceptions
#syntax error ==> programming syntax error in python
#Logical Error ==> it's not a coding error but developer logical error(Output is not match is called a Logical Error)
#Runtime Error ==>
'''
n = 10
d = 0
result = n/d
print(result)

x = 5
y = z+3
print(x)
print(y)
'''

#Exception handle

n = int(input("Enter a number:"))
d = int (input("Enter a number:"))
result = 0
try:
    result = n/d
except ZeroDivisionError:
    print("You can't divide by zero")

print(result)
