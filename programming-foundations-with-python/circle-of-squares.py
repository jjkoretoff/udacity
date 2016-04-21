#build a circle by rotating a square

import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create a turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed("fast")
    #want to create loop to repeat
    for i in range(1, 36):
    #call the draw_square function/loop we wrote above for brad
        draw_square(brad)
    #make the turtle turn by a certain number of degrees
        brad.right(10)
    window.exitonclick

draw_art()
    
