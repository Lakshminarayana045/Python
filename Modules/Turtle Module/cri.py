from turtle import *
color("blue", "green", "orange", "purple", "white" )
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
        end_fill()
    done()
