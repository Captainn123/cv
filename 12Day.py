import random
def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number= random.randint(1, 100)
    print(number)
    def easy():
        chances=5
        while chances !=0:
            print(f"You have {chances} attempts remaining to guess number.")
            guess=int(input("Make a guess:"))
            if guess==number:
                print("You guess right. You win")
                return True
            else:
                chances =chances-1
        if chances==0:
            print("You Lose") 
            return False  
    def hard():
        chances=2
        while chances !=0:
            print(f"You have {chances} attempts remaining to guess number.")
            guess=int(input("Make a guess:"))
            if guess==number:
                print("You guess right. You win")
                break
            else:
                chances =chances-1
        if chances==0:
            print("You Lose")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty=='easy':
        easy()
    elif difficulty=='hard':
        hard()
    else:
        print("Enter valid input")
    choice=input("Do You want to play again? y for yes or n for no")
    if choice=='y':
        play_game()
    else:
        print("Thanks")
    
play_game()