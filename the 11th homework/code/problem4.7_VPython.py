#	-*- coding: utf-8 -*-
from visual import *
import time
import math

#	set parameter
r = 0
m1 = 100.0
m2 = 500.0
dt = 0.002

#	create two Planets
p1 = sphere(pos=(1,0,0), radius=0.1, color=color.red)
p2 = sphere(pos=(-1,0,0), radius=0.5, color=color.yellow)
ground = box(pos=(0,0,0),length=3,height=3,width=3,opacity=0)

p1.velocity = vector(0, 0, 0)
p1.velocity.x = 0
p1.velocity.y = 10.0

p2.velocity = vector(0, 0, 0)
p2.velocity.x = 0
p2.velocity.y = -2.0

while 1:
	#	设置动画速度
	rate(100)
	
	#	导弹飞行轨迹
	r = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)

	p1.velocity.x += m2*(p2.x-p1.x)/(r**3)*dt
	p1.velocity.y += m2*(p2.y-p1.y)/(r**3)*dt
	p2.velocity.x += m1*(p1.x-p2.x)/(r**3)*dt
	p2.velocity.y += m1*(p1.y-p2.y)/(r**3)*dt

	p1.x += p1.velocity.x*dt
	p1.y += p1.velocity.y*dt
	p2.x += p2.velocity.x*dt
	p2.y += p2.velocity.y*dt