import turtle

length = 100

def move_to(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

def draw_ieung():
        x, y = turtle.pos()
        turtle.setheading(0)
        turtle.left(180)
        turtle.circle(length * 0.5)
        move_to(x, y)

def draw_yoo():
        x, y = turtle.pos()
        y2 = y - length * 1.5
        move_to(x - length, y2)
        turtle.setheading(0)
        turtle.forward(length * 2)
        turtle.backward(length * 1.3)
        turtle.right(90)
        turtle.forward(length)
        move_to(x + length * 0.3, y2)
        turtle.forward(length)
        move_to(x, y)

def draw_nieun():
        x, y = turtle.pos()
        move_to(x - length * 0.5, y)
        turtle.setheading(0)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        move_to(x, y)

def draw_siot():
        x, y = turtle.pos()
        turtle.setheading(0)
        turtle.right(120)
        turtle.forward(length)
        turtle.backward(length * 0.6)
        turtle.left(60)
        turtle.forward(length * 0.6)
        move_to(x, y)

def draw_eu():
        x, y = turtle.pos()
        move_to(x - length, y - length * 1.5)
        turtle.setheading(0)
        turtle.forward(length * 2)
        move_to(x, y)

def draw_kiyeok():
        x, y = turtle.pos()
        turtle.setheading(0)
        turtle.backward(length * 0.5)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        move_to(x, y)

def next_letter():
        x, y = turtle.pos()
        x = x + length * 2.1
        move_to(x, y)

def final_letter(func = None):
        x, y = turtle.pos()
        if func != None:
                move_to(x, y - length * 2.5)
                func()
                move_to(x, y)
        next_letter()

move_to(length * -3, length * 4)

draw_ieung()
draw_yoo()
final_letter(draw_nieun)

draw_siot()
draw_eu()
final_letter(draw_ieung)

draw_kiyeok()
draw_yoo()
next_letter()

turtle.exitonclick()
