import turtle
import time
import random

delay = 0.1
wn = turtle.Screen()
wn.title("Naag by @Utsav Stha")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('red')
head.penup()
head.goto(0,0)
head.direction= 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('green')
food.penup()
food.goto(0,100)

segments = []

# Snake Food
def go_up():
    head.direction="up"
def go_down():
    head.direction="down"
def go_left():
    head.direction="left"
def go_right():
    head.direction="right"
def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x = head.xcor()
        head.setx(x+20)


#ksyword bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')
# Main game
while True:
    wn.update()
    # check for a collision
    if head.distance(food)< 20: 
        #Move the food at random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

    for index in range (len(segments)-1,0,-1 ):
        x= segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0]. goto(x,y)
    move()
    time.sleep(delay)

wn.mainloop()