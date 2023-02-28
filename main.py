import turtle as turtle_module
import random

turtle_module.colormode(255)
quang_the_turtle = turtle_module.Turtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
              (168, 99, 102)]

# quang_the_turtle.forward(200)
# quang_the_turtle.penup()
# quang_the_turtle.goto(0, 20)
# quang_the_turtle.pendown()
#
# quang_the_turtle.forward(200)
# quang_the_turtle.penup()
# quang_the_turtle.goto(0, 40)
# quang_the_turtle.pendown()
#
# quang_the_turtle.forward(200)
# quang_the_turtle.penup()
# quang_the_turtle.goto(0, 60)
# quang_the_turtle.pendown()


# quang_the_turtle.dot(20, 'red')
# quang_the_turtle.penup()
# quang_the_turtle.forward(30)
# quang_the_turtle.pendown()
# quang_the_turtle.dot(20, 'red')

quang_the_turtle.speed(0)
screen = turtle_module.Screen()

screen.screensize(canvwidth=500, canvheight=500, bg='black')


def move_right():
    for _ in range(13):
        quang_the_turtle.dot(20, random.choice(color_list))
        quang_the_turtle.penup()
        quang_the_turtle.forward(75)
        quang_the_turtle.pendown()


def set_X_position(position):
    quang_the_turtle.penup()
    quang_the_turtle.setx(position)
    quang_the_turtle.pendown()
    return position


def set_Y_position(position):
    quang_the_turtle.penup()
    quang_the_turtle.sety(position)
    quang_the_turtle.pendown()
    return position


start_position_x = set_X_position(-500)
start_position_y = set_Y_position(-350)
for i in range(25):
    move_right()
    start_position_y += 30
    quang_the_turtle.penup()
    quang_the_turtle.goto(start_position_x, start_position_y)
    quang_the_turtle.pendown()

screen.exitonclick()
