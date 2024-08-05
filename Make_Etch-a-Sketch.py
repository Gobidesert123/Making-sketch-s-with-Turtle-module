
'''
Requirements:

w = forwards
s = backwords
a = couter-clockwise
d =  clockwise
c = clear drawing

'''
# importing
from turtle import Turtle, Screen

# Creating objects
tim = Turtle()
screen = Screen()

# Creating functions
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear():
    tim.reset()

# This is so the screen can read the keys we press on keyboard
screen.listen()

# These functions are called upon once the key is pressed.
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clockwise, 'd')
screen.onkey(clear, 'c')

# This is so the screen exists on click
screen.exitonclick()