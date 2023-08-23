import random
import string

length =random.randint(0,9)
word = ''.join(random.choices(string.ascii_lowercase, k=length))
# print("Random word:", word)
# word="rajat"
lives=len(word)
for i in range(0,len(word)):
    name=input("Enter any Char")
    if name in word and name== word[i]:
        print("You are right")
    else:
        print("You are wrong and you loose your 1 life")
        lives=lives-1
        print(f"you have {lives} lives remaining")
        if lives==0:
            print("Game Over")
            break
if lives>0:
    print("You Win")