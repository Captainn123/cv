import turtle as t
from turtle import Screen
import random
tim=t.Turtle()
tim.shape("turtle")
# tim.color("green")
# colours=["Red","Green","Blue","Yellow"]
# def draw_shape(no_of_sides):
#     angle=360/no_of_sides
#     for _ in range(no_of_sides):
#         tim.forward(50)
#         tim.right(angle)
# for value in range (3,11):
#     tim.color(random.choice(colours))
#     draw_shape(value)
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_tuple=(r,g,b)
    return my_tuple
tim.speed("fastest")
angle=1
for _ in range(360):
    tim.color(random_color())
    tim.circle(100)
    tim.right(angle)
    angle +=1

# direction=["left","right"]
# for _ in range(200):
#     tim.color(random_color())
#     value=random.choice(direction)
#     angel=random.choice(0,90,180,270,360)
#     tim.width(10)
#     tim.forward(20)
#     if value == "left":
#         tim.left(angel)
#     elif value == "right":
#         tim.right(angel)







screen = Screen()
screen.exitonclick()