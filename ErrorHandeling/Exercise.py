def divider(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("You can't divide by zero")
        return 0

print(divider(1,3))