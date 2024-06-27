import turtle

sc = turtle.Screen()

sc.setup(width=1000, height=600)

ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.shapesize()
ball.penup()
#ball.goto(0, 0)
ball.dx = 5
ball.dy = -5


while True:
    sc.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 280:
	    ball.sety(280)
	    ball.dy *= -1

    if ball.ycor() < -280:
	    ball.sety(-280)
	    ball.dy *= -1

    if ball.xcor() > 480:
	    ball.setx(480)
	    ball.dx *= -1

    if ball.xcor() < -480:
	    ball.setx(-480)
	    ball.dx *= -1
