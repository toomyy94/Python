# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

with open("drawing.txt", "r") as cmds:
    for line in cmds:
        if line == "UP\n":
            t.up()
        elif line == "DOWN\n":
            t.down()
        else:
            t.goto(int(line.split()[0]), int(line.split()[1]))

 
turtle.Screen().exitonclick()

