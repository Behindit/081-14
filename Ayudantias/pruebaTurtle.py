from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

###

ht()
penup()
setpos(-200, -200)
pendown()
st()
speed(0)
d = 0

###

color('black')

for c in range(4):
    d += 1
    if (c != 0):
        ht()
        penup()
        setpos(-200, -200+(50*(d)))
        pendown()
        st()
    for b in range(4):
        begin_fill()
        for a in range(4):
            forward(50)
            right(90)
        end_fill()
        forward(50)
        for a in range(4):
            forward(50)
            right(90)
        forward(50)
    ht()
    penup()
    if d > 1:
        d += 1
    setpos(-200, -200+(50*(d)))
    pendown()
    st()
    for b in range(4):

        for a in range(4):
            forward(50)
            right(90)

        forward(50)
        begin_fill()
        for a in range(4):
            forward(50)
            right(90)
        end_fill()
        forward(50)


done()
