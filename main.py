from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fwd():
    tim.forward(10)
def move_back():
    tim.back(10)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.speed(0)
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key = "w", fun = move_fwd)
screen.onkeypress(key = "s", fun = move_back)
screen.onkeypress(key = "d", fun=turn_right)
screen.onkeypress(key = "a" , fun = turn_left)
screen.onkeypress(key = "c", fun = clear)











screen.exitonclick()