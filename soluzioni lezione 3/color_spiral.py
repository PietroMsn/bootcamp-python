import turtle as t
colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']

for x in range(360):
    t.pencolor(colors[x % 6])
    t.forward(x)
    t.left(20)
