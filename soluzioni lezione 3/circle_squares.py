import turtle


sc = turtle.Screen()
sc.bgcolor('black')
colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green', 'white', 'cyan']

raggio = 100


iterazioni = 50

for i in range(iterazioni):
    turtle.pencolor(colors[i % 8])
    turtle.circle(raggio, 360, 7) 
    
    turtle.left(360 / iterazioni)
