def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a/b)

first_number = float(input("enter first number of operation: "))
operator = input("enter operator(+,-,*,/): ")
second_number = float(input("enter second number of operation: "))

if operator == "+":
    add(first_number, second_number)
elif operator == "-":
    subtract(first_number,second_number)
elif operator == "*":
    multiply(first_number,second_number)
elif operator == "/":
    divide(first_number)
else:
    print("invalid operator")