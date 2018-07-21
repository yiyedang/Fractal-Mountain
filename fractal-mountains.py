'''
Created on Jul 15, 2018

@author: yiyedang
'''
import random
import turtle

def getMid(p1, p2 ,l):
    r = random.randrange(-l // 5 *6 , l // 5 *6)
    return  ((p1[0]+p2[0]) // 2, (p1[1] + p2[1]) // 2 + r)

def mountain(t, p1, p2, length, depth):
    if depth == 0:
        t.goto(p1)
        t.goto(p2)
    else:
        mid = getMid(p1, p2, length//2)
        mountain(t, p1, mid, length//2, depth - 1)
        mountain(t, mid, p2, length//2, depth - 1)
    
    
t = turtle.Turtle()
wn = turtle.Screen()
t.speed(1)  
myPoints = [[-300,0], [300,0]]
t.up()
t.goto(myPoints[0])
t.down()
mountain(t, myPoints[0], myPoints[1], 300, 5)

wn.exitonclick()
