# from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
# This project has to consist on the user being able to draw out a sketch while using 'w,a,s,d' keys


tim = turtle.Turtle()
screen = turtle.Screen()
tim.speed("slowest")


def change_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    turtle.color(r, g, b)


def randomize():
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.ontimer(randomize)


def move_forward():
    tim.forward(30)


def move_backwards():
    tim.backward(30)


def move_right():
    """This is another method to turn right"""
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)


def move_left():
    """This is another method to turn left"""
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.speed("fastest")
    tim.penup()
    tim.home()
    tim.pendown()


turtle.colormode(255)
screen.setup(1000, 1000)

screen.listen()
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backwards, 's')
screen.onkey(lambda: tim.tilt(20), 'd')
screen.onkey(lambda: tim.right(20), 'd')
screen.onkey(lambda: tim.tilt(-20), 'a')
screen.onkey(lambda: tim.left(20), 'a')
screen.onkey(clear, 'c')

screen.listen()

turtle.done()
