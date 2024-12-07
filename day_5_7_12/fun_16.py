import turtle

t = turtle.Turtle()
t.speed(-1)
t.setheading(90)
t.penup()
t.goto(0, -200)
t.pendown()


def braanch(t, len):
    if len == 0: return
    nt = t.clone()
    nt.forward(50)
    nt.left(20)
    braanch(nt, len - 1)
    nt.right(40)
    nt.forward(20)
    braanch(nt, len - 1)


braanch(t, 7)
window = turtle.Screen()
window.exitonclick()
