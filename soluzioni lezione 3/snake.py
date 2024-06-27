import turtle
import random as r

sc = turtle.Screen()
vel = 5
w, h = 1000, 600
sc.setup(width=w, height=h)

player = turtle.Turtle()
player.speed(1000)
player.shape("square")
player.color("green")
player.penup()
player.dx = 5
player.dy = 0


target = turtle.Turtle()
target.speed(0)
target.shape("circle")
target.color("orange")
target.penup()
target.goto(r.randint(-w/2 + 10, w/2 - 10), r.randint(-h/2 + 10, h/2 -10))


def paddleup():
    if player.dy == 0:
        player.dy = vel
        player.dx = 0
    if player.dy < 0:
        player.dy *= -1
        player.dx = 0


def paddledown():
    if player.dy == 0:
        player.dy = -vel
        player.dx = 0
    if player.dy > 0:
        player.dy *= -1
        player.dx = 0

def paddleright():
    if player.dx == 0:
        player.dx = vel
        player.dy = 0
    if player.dx < 0:
        player.dx *= -1
        player.dy = 0
        
def paddleleft():
    if player.dx == 0:
        player.dx = -vel
        player.dy = 0
    if player.dx > 0:
        player.dx *= -1
        player.dy = 0

sc.listen()
sc.onkeypress(paddleup, 'Up')
sc.onkeypress(paddledown, 'Down')
sc.onkeypress(paddleleft, 'Left')
sc.onkeypress(paddleright, 'Right')

while True:
    sc.update()

    player.setx(player.xcor() + player.dx)
    player.sety(player.ycor() + player.dy)

    if player.xcor() < target.xcor() + 20 and player.xcor() > target.xcor() - 20 and target.ycor() < player.ycor() + 20 and target.ycor() > player.ycor() - 20:
        
        target.goto(r.randint(-w/2+10, w/2-10), r.randint(-h/2+10, h/2-10))
        vel += 1

    if player.xcor() > w/2  or player.xcor() < -w/2  or player.ycor() < -h/2  or player.ycor() > h/2 :
        player.goto(0,0)
        vel = 5

        


    
