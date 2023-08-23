# student_scores={"Harry":81, "Ron":78, "Hermione":99, "Draco":74, "Neville":62}
# for i in student_scores:
#     if student_scores[i]>90:
#         print(f"{i} done outstanding 91+")
#     elif student_scores[i]>80:
#         print(f"{i} done Exceeds Expectations 81+")
#     elif student_scores[i]>70:
#         print(f"{i} done Acceptable 71+")
#     else :
#         print(f"{i} done Fail 70-")

list_bidders={}
bidding_finished=False
while bidding_finished==False:
    name=input("What is your name?")
    bid=int(input("What is your bid"))
    list_bidders[name]=bid
    carry_on=input("are they any other bidders? yes or no")
    if carry_on=="no":
        bidding_finished=True
highest_bid=0
for i in list_bidders:
    if highest_bid<list_bidders[i]:
        highest_bid=list_bidders[i]
        highest_bidder=i
print(f"Highest bidder {highest_bidder} wins with {highest_bid} bid")


    
 
