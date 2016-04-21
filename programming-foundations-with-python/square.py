
# drawing a square
# turtle graphics
# open window
# cycle through comands

import turtle

def brad_turtle():
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed("slow")

    for i in [0, 1, 2, 3]:
        brad.forward(100)
        brad.right(90) #angle

brad_turtle()

def angie_turtle():
    
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("yellow")
    angie.speed("slow")
    angie.circle(100)

angie_turtle()

def carl_turtle():

    carl = turtle.Turtle()
    carl.shape("arrow")
    carl.color("green")
    carl.speed("slow")

    for i in [0, 1, 2]:
        carl.forward(200)
        carl. left(120) #angle

carl_turtle()


window = turtle.Screen()
window.bgcolor("black")
window.exitonclick()
