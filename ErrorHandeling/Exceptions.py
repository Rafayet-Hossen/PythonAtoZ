n = int(input("Enter a number:"))
d = int (input("Enter a number:"))
result = 0
try:
    result = n/d
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(result)
finally:
    print("Thanks for using this program")
