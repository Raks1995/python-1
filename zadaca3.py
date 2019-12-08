a = int(input("Broj 1: "))
b = int(input("Broj 2: "))

operation = input ("Operation (+,-,*,/): ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Can't process, try again")

