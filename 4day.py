import random
# rando= random.randint(0,1)
# if rando==0:
#     print("Heads")
# else:
#     print("Tails")

print("Welcome to Rock, Paper, Scissor")
choice=int(input("Enter 0, 1, 2 for Rock, Paper, Scissor"))
server_choice=['rock', 'paper', 'scissor']
number=len(server_choice)
rando= random.randint(0, number-1)
if choice==rando:
    print("It is a Tie, Try Again")
elif choice==0 and rando==1:
    print("Server won")

elif choice==0 and rando==2:
    print("Rajat won")
elif choice==1 and rando==0:
    print("Rajat won")
elif choice==1 and rando==2:
    print("Server won")
elif choice==2 and rando==0:
    print("Server won")
elif choice==2 and rando==1:
    print("Rajat won")
else:
    print("Value Error")
