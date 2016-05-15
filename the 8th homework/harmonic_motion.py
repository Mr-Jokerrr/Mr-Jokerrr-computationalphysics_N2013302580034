#	-*- coding: utf-8 -*-
from visual import *


k = 1
alpha = 1
dt = 0.01
wall_bottom = box(pos=(0,0,0), size=(15, 5, 0.1), color=color.green, opacity = 0)
ball = sphere(pos=(0,0,2), radius=1, color=color.red)
ball.velocity = vector(0, 0, 0)
ball.velocity.x = 5
bv = arrow(pos = ball.pos, axis=ball.velocity*0.5, color=color.yellow)


while 1:
	rate(100)
	a = -k*ball.pos.x**alpha
	ball.velocity.x += a*dt
	ball.pos.x += ball.velocity.x*dt
	
	bv.pos = ball.pos
	bv.axis.x = ball.velocity.x*0.5