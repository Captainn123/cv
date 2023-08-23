# import math
# wall_height=int(input("Enter Wall Height"))
# wall_widtht=int(input("Enter Wall Width"))
# coverage=5
# def wall_paint(height, width, cover):
#     area_of_wall=height*width
#     no_of_cans=math.ceil(area_of_wall/cover)
#     print(f"You need {no_of_cans} cans to paint on wall")

# wall_paint(wall_height, wall_widtht, coverage)

# num=int(input("Enter a Number"))
# def check_prime(n):
#     for i in range (2,10):
#        if n%i==0 and n!=i:
#            print("Not a Prime Number")
#            break
#        else:
#            print("It is a Prime number")
#            break
# check_prime(num)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
shift = int(input("Enter a number to shift letters: "))
print("Original letters:", letters)


def shift_letters(num):
    shifted_letters = letters[shift:] + letters[:shift]
    print("Shifted letters:", shifted_letters)


shift_letters(shift)