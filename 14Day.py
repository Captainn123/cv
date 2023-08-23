from game_data import data
import random
times=5
score=0
def play_game():
    global times
    global score
    while times!=0:
        a=random.choice(data)
        b=random.choice(data)
        print(a)
        print(b)
        
        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
        def comapare_follower(input_A, input_B):
        
            if input_A['follower_count']>input_B['follower_count']:
                
                return 'A'
            else:
                
                return 'B'
        result=comapare_follower(a,b)
        
        
        value=input("Who has more followers? Type 'A' or 'B':")
        if value==result:
                score +=1
                times -=1
                print(f"You are right. Your final score is {score}")
        else:
                times -=1
                print(f"You are wrong. Your final score is {score}")
        play_game()
    
play_game()
