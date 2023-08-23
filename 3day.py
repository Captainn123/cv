# # num= int(input("Enter a number"))
# # if num%2==0:
# #     print(num, "is even Number")
# # else:
# #     print(num,"is odd number")

# print("Welcome to Pizza Deleiveries")
# size=input("What size of pizza do you want?S,M orL")
# if size=='S':
#     size=15
#     add_pepperoni=input("Do you want pepperoni?Y or N")
#     if add_pepperoni=='Y':
#         result=size+2
#     else:
#         result=size
    
# elif size=='M':
#     size=20
#     add_pepperoni=input("Do you want pepperoniY or N?")
#     if add_pepperoni=='Y':
#         result=size+3
#     else:
#         result=size
# elif size=='L':
#     size=25
#     add_pepperoni=input("Do you want pepperoniY or N?")
#     if add_pepperoni=='Y':
#         result=size+3
#     else:
#         result=size
# else:
#     print("Size not available")
    

# extra_cheese=input("Do you want extra cheese?Y or N")
# if extra_cheese=='Y':
#     final_result=result+1
# else:
#     final_result=result
# print("Your bill is",final_result)

# print("Welcome to love calculator")
# name1=input("What is your name")
# name2=input("What is their name")
# total_name=name1+name2
# lower_total_name=total_name.lower()
# t=lower_total_name.count("t")
# r=lower_total_name.count('r')
# u=lower_total_name.count('u')
# e=lower_total_name.count('e')
# true=t+r+u+e
# l=lower_total_name.count('l')
# o=lower_total_name.count('o')
# v=lower_total_name.count('v')
# e=lower_total_name.count('e')
# love=l+o+v+e
# love_score=str(true)+str(love)
# print("Your love score is "+love_score+"%")

print("Welcome to Treasure Island")
stage_one=input("Enter left or right")
if stage_one=='left':
    stage_two=input("Enter wait or swim")
    if stage_two=='wait':
        stage_three=input("Which door you choose?red, blue or yellow")
        if stage_three=='yellow':
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")


