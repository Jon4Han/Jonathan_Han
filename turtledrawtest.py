import random
import turtle 

screen = turtle.Screen()
screen.setup(1200,1100)

random.seed(2023)
t= turtle.Turtle()
t.speed(0)
t.color("black")

# Draw the X-axis.
##  comment 
t.up()
t.goto(-500, 0)
t.down()
t.forward(1000)
t.up()

# Draw the Y-axis.
t.goto(0, -500)
t.down()
t.right(270)
t.forward(1000)
t.up()

#turtle.done()

COLORS = ["beige", "coral", "gold", "blue", "green"]

t.goto(50,0)


for i in range(30):
    color_index = random.randint(0,len(COLORS)-1)
    selected_color = COLORS[color_index]
    t.setheading(90) 
    #t.goto(50*(i+1),0)
    t.color(selected_color)
    t.pendown()
    t.circle(50+i*10)
    t.penup()
    t.goto(50+10*(i+1),0)
t.goto(340,0)  
t.pendown()
t.color("red")
t.setheading(90)
t.forward(340)
t.left(90)
t.forward(680) 
t.left(90)
t.forward(680)
t.left(90)
t.forward(680)
t.left(90)
t.forward(340) 
t.hideturtle()

screen.mainloop()

