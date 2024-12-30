import turtle
turtle.color('green','yellow')
turtle.begin_fill()
while True:
    turtle.speed(50)
    turtle.forward(250)
    turtle.left(165)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()