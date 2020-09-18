import turtle

size = 100
amount = 5
count1, count2 = amount, amount

x, y = turtle.pos()

while (count1 >= 0):
    turtle.penup()
    turtle.goto(count1 * size, 0)
    turtle.pendown()
    turtle.goto(count1 * size, amount * size)
    count1 = count1 - 1

while (count2 >= 0):
    turtle.penup()
    turtle.goto(0, count2 * size)
    turtle.pendown()
    turtle.goto(amount * size, count2 * size)
    count2 = count2 - 1

turtle.exitonclick()
