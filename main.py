num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
print("What axtion would you like to carry out:")
exec = input("1. Multiplication  2. Division  3. Addition  4. Subtraction")

if exec == ("Multiplication"):
    result = float(num1)*float(num2)
    print(result)
elif exec == ("Division"):
     result = float(num1) / float(num2)
     print(result)
elif exec == ("Addition"):
    result = float(num1) + float(num2)
    print(result)
elif exec == ("Subtraction"):
    result = float(num1) - float(num2)
    print(result)
else:
    print("Invalid action, try again.")
