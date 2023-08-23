def add_num(number1,number2):
    a=number1+number2
    print(f"{number1}+{number2}=",a)

def sub_num(number1,number2):
    b=number1-number2
    print(f"{number1}-{number2}=",b)

def mul_num(number1,number2):
    c=number1*number2
    print(f"{number1}*{number2}=",c)

def div_num(number1,number2):
    d=number1/number2
    print(f"{number1}/{number2}=",d)

first_number=int(input("Enter your first number"))
print("+\n-\n*\n/\n")
operation=input("Pick an operation:")
if operation=="+":
    second_number=int(input("Enter your second number"))
    add_num(first_number, second_number)
elif operation=="-":
    second_number=int(input("Enter your second number"))
    sub_num(first_number, second_number)
elif operation=="*":
    second_number=int(input("Enter your second number"))
    mul_num(first_number, second_number)
elif operation=="/":
    second_number=int(input("Enter your second number"))
    div_num(first_number, second_number)
else:
    print("Invalid Pick")