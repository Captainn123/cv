# print("Welcome to tip calculator")
# bill= int(input("What is the total bill"))
# person=int(input("In how many people to split bill"))
# tip=int(input("What percent tip would you like to give"))
# tip_result=(bill*tip)/100
# result=(bill+tip_result)/person
# print("Each person should pay:",result)

# num=input("Enter any Number")
# num1=num[0]
# num2=num[1]
# result=int(num1) + int(num2)
# print(result)

weight=input("Enter your weight in kg")
height=input("enter yor height in meter")
bmi=int(weight)/float(float(height)** 2)
if bmi<20:
    print("You are under weight and your BMI is ",bmi)
elif bmi==20:
    print("You are fit")
else :
    print(f"You are over weight and your BMI is {bmi}")