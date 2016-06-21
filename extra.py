#	-*- coding: utf-8 -*-
from visual import *
import time
import math
import random

#	获取高斯分布随机数（采用Box-Muller方法）
def get_gaussian(miu, sigma):
	G = math.sqrt(-2*math.log(random.random()))*math.cos(2*math.pi*random.random())
	return miu + (G*sigma)

#	获取随机值
def get_random(size, uncertainty):
	G = get_gaussian(uncertainty*100,1)
	return 2*size*G/100*random.random()+size*(1-G/100)

#	set parameter
k = 252.82
dt = 0.001
i = 0
j = 0
n = 50	#分子数
R_temp = 0
B = []
aBx = [0 for row in range(n)]
aBy = [0 for row in range(n)]
aBz = [0 for row in range(n)]

for i in range(n):
	B.append(0)
	B[i]=sphere(pos=((-10+20*random.random()),(-10+20*random.random()),(-10+20*random.random())), radius=0.1, color=color.red)#随机创建分子
	B[i].velocity=vector(100*get_random(1,5),100*get_random(1,5),100*get_random(1,5))

ground = box(pos=(0,0,0),length=20,height=20,width=20,opacity=0.05)

while 1:
	rate(100)
	for i in range(n):
		aBx[i] = aBy[i] = aBz[i] = 0
	for i in range(n):
		for j in range(n):
			if i!=j:
				R_temp=sqrt((B[i].x-B[j].x)**2+(B[i].y-B[j].y)**2+(B[i].z-B[j].z)**2)
				aBx[i] += k*(B[i].x-B[j].x)/R_temp**3
				aBy[i] += k*(B[i].y-B[j].y)/R_temp**3
				aBz[i] += k*(B[i].z-B[j].z)/R_temp**3

	for i in range(n):
		B[i].velocity.x += aBx[i]*dt
		B[i].velocity.y += aBy[i]*dt
		B[i].velocity.z += aBz[i]*dt
			
		if B[i].x>=10:
			B[i].x=20-B[i].x
			B[i].velocity.x = -B[i].velocity.x
		if B[i].x<=-10:
			B[i].x=-20-B[i].x
			B[i].velocity.x = -B[i].velocity.x
		if B[i].y>=10:
			B[i].y=20-B[i].y
			B[i].velocity.y = -B[i].velocity.y
		if B[i].y<=-10:
			B[i].y=-20-B[i].y
			B[i].velocity.y = -B[i].velocity.y
		if B[i].z>=10:
			B[i].z=20-B[i].z
			B[i].velocity.z = -B[i].velocity.z
		if B[i].z<=-10:
			B[i].z=-20-B[i].z
			B[i].velocity.z = -B[i].velocity.z
			
		B[i].pos += B[i].velocity*dt