import turtle

a = int(input('輸入正多邊形邊數'))
b = turtle.Turtle()

for i in range(a):
    b.forward(100)
    b.left(360/a)
turtle.done()
