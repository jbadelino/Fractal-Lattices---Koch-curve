# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:33:12 2018

@author: Asus
"""

#import turtle graphics for an easier drawing environment 
import turtle 


#define a function for constucting a Koch curve 
def Koch_curve1(length, iteration):
    if iteration > 0:
        for theta in [-60, 120, -60, 0]:
            Koch_curve1(length/3,iteration-1)
            turtle.right(theta)
    else:
        turtle.forward(length)
        
def Koch_curve2(length, iteration):
    if iteration > 0:
        for theta in [-60, 120, -60, 0]:
            Koch_curve2(length/3, iteration-1)
            turtle.left(theta)
    else:
        turtle.forward(length)

#set the size and the level number
size = 500
iteration = 5

#places the Koch curve at the center of the drawing screen 
turtle.penup()
turtle.backward(size/1.8)
turtle.left(30)
turtle.pendown()


#choose a color for the background and the Koch curve 
turtle.color("black", "white")
turtle.bgcolor("white")


#set the speed for drawing the curve 
turtle.tracer(10)

turtle.begin_fill()

#draw three Koch curves 
#if level is 0, an equilateral triangle will be drawn
for n in range(3):
    turtle.pensize(3)
    Koch_curve1(size, iteration)
    #Koch_curve2(size, iteration)
    turtle.right(120)

turtle.end_fill()

#update the turtle screen to show the latest parts 
turtle.update()

#saves the turtle canvas as a postscript file 
turtle.getscreen().getcanvas().postscript(file='as5.ps')
turtle.done()