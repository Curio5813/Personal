from turtle import *


speed('fast')
rt(-90)
angle = 25


def y(sz, level):
    if level > 0:
        colormode(255)
        pencolor(0, 255 // level, 0)
        fd(sz)
        rt(angle)
        y(0.8 * sz, level - 1)
        pencolor(0, 255 // level, 0)
        lt(2 * angle)
        y(0.8 * sz, level - 1)
        pencolor(0, 255 // level, 0)
        rt(angle)
        fd(-sz)


y(80, 10)


