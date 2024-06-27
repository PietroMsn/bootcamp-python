import turtle
import random as r

sc = turtle.Screen()

w, h = 1000, 600
vel = 20
sc.setup(width=w, height=h)

player = turtle.Turtle()
player.speed(1000)
player.shape("square")
player.color("green")
#player.shapesize(stretch_wid=6, stretch_len=2)
player.penup()

target = turtle.Turtle()
target.speed(0)
target.shape("circle")
target.color("orange")
target.penup()
target.goto(r.randint(-w/2 + 10, w/2 - 10), r.randint(-h/2 + 10, h/2 -10))


score = 0
'''
score_text = turtle.Turtle()
score_text.speed(0)
score_text.color("black")
score_text.penup()
score_text.hideturtle()
score_text.goto(0, h / 2 - 40)
score_text.write("hai raggiunto uno score di " + str(score), align="center", font=("Courier", 24, "normal"))
'''




def paddleup():
	y = player.ycor()
	y += vel
	player.sety(y)


def paddledown():
	y = player.ycor()
	y -= vel
	player.sety(y)

def paddleright():
	x = player.xcor()
	x += vel
	player.setx(x)

def paddleleft():
	x = player.xcor()
	x -= vel
	player.setx(x)



sc.listen()
sc.onkeypress(paddleup, "Up")
sc.onkeypress(paddledown, "Down")
sc.onkeypress(paddleright, "Right")
sc.onkeypress(paddleleft, "Left")

while True:
        sc.update()

        if score == 10:
                sc.bye()
        
        if player.xcor() < target.xcor() + 20 and player.xcor() > target.xcor() - 20 and target.ycor() < player.ycor() + 20 and target.ycor() > player.ycor() - 20:
                target.goto(r.randint(-w/2+10, w/2-10), r.randint(-h/2+10, h/2-10))
                score += 1
                '''
                score_text.clear()
                score_text.write("hai raggiunto uno score di " + str(score), align="center", font=("Courier", 24, "normal"))
                '''
                #vel +=5
