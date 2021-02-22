num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
print("What axtion would you like to carry out:")
exec = input("1. Multiplication  2. Division  3. Addition  4. Subtraction")

if exec == ("Multiplication"):
    result = num1*num2
    print(result)
elif exec == ("Division"):
     result = num1 / num2
     print(result)
elif exec == ("Addition"):
    result = num1 + num2
    print(result)
elif exec == ("Subtraction"):
    result = num1 - num2
    print(result)
else:
    print("Invalid action, try again.")
