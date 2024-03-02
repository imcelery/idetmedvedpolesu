# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             f = b == (a or (c <= b))
#             f2 = b == ((a or c) <= b)
#             if f and f2:
#                 print(a, b, c)

# def f(x):
#     x = str(x)
#     s = 0
#     for i in range(16):
#         if i % 2 != 0:
#             s += int(x[i])
#         else:
#             a = int(x[i]) * 2
#             if a >= 10:
#                 a = a // 10 + a % 10
#             s += a
#     if s % 10 == 0:
#         print(s)
#         return True
#
#     else:
#         return False
# for i in range(1234_5678_9101_1122, 2000_0000_0000_0000):
#     if f(i):
#         print(i)
#         break

import turtle
scale = 10
turtle.penup()
turtle.goto(-3 * scale, -4 * scale)
turtle.pendown()

turtle.color("red")
turtle.hideturtle()

turtle.left(90)
turtle.speed(100)
turtle.pensize(scale / 4)

turtle.begin_fill()

turtle.right(30)
for i in range(3):
    turtle.forward(14 * scale)
    turtle.right(120)

turtle.end_fill()


can = turtle.getcanvas()
turtle.up()
c = 0
for x in range(-10 * scale, 10 * scale, scale):
    for y in range(-10 * scale, 10 * scale, scale):
        turtle.goto(x, y)
        s = can.find_overlapping(x, y, x, y)
        print(s)
        turtle.dot(3, "black")



print(c)
