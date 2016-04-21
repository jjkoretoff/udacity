#build a circle by rotating a square

import turtle

def draw_triangle(some_turtle):
    for i in range(1, 4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create a turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed("fast")
    #want to create loop to repeat
    for i in range(1, 18):
    #call the draw_square function/loop we wrote above for brad
        draw_triangle(brad)
    #make the turtle turn by a certain number of degrees
        brad.right(20)
    brad.circle(50)
    brad.home()
    brad.seth(270)
    brad.forward(200)
    window.exitonclick

draw_art()
