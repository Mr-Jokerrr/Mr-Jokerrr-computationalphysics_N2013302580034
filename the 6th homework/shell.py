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


print "Please enter the velocity"
input_v = float(raw_input())
print "Please enter the uncertainty"
input_unc = float(raw_input())
v = get_random(input_v, input_unc)	#	速度含误差

#	设置基本参数
dt = 0.01
g = 9.8
temp_theta = 0


#	设置参数
blast_radius = 3
target_radius = 0.5
target_x = 10
target_z = 10
k = get_random(1,0.1)	#	风阻误差


#	以45°，设置的初速的的110%，不计风阻发射的最远距离，如果达不到，则弹出提示
test_t = v*1.1/math.sqrt(2)/g
test_x = v*1.1/math.sqrt(2)*test_t
test_l = math.sqrt(target_x**2+target_z**2)
if test_x < test_l:
	print "Can't hit the target"
	
	
	
else:
	#	创建炮弹、地面、目标
	shell = sphere(pos=(0,-10,0), radius=0.5, color=color.yellow)
	wall_front = box(pos=(0,-10,0), size=(40, 0.1, 40), color=color.green, opacity = .2)
	target = sphere(pos=(target_x, -10, target_z), radius=target_radius, color=color.red)
	
	v = get_random(input_v, input_unc)
	theta = get_random(temp_theta,0.01)
	shell.velocity = vector(0, 0, 0)
	temp_v = v
	shell.velocity.x = temp_v*math.cos(theta/180*math.pi)*target_x/math.sqrt(target_x**2+target_z**2)
	shell.velocity.y = temp_v*math.sin(theta/180*math.pi)
	shell.velocity.z = temp_v*math.cos(theta/180*math.pi)*target_z/math.sqrt(target_x**2+target_z**2)
	
	
	#	创建数组储存满足要求的炮弹的初始速度
	theta_right = []
	
	
	#	使用VPython模拟	
	i=0
	
	while i < 1000000:
		#	设置动画速度
		rate(400)
		
		
		#	炮弹飞行轨迹
		temp_v = math.sqrt(shell.velocity.x**2+shell.velocity.y**2+shell.velocity.z**2)
		shell.pos += shell.velocity*dt
		shell.velocity.x -= (1-(0.0065*shell.pos.y)/288)**2.5*k*0.04*temp_v*shell.velocity.x*dt
		shell.velocity.y -= (1-(0.0065*shell.pos.y)/288)**2.5*k*0.04*temp_v*shell.velocity.y*dt + g*dt
		shell.velocity.z -= (1-(0.0065*shell.pos.y)/288)**2.5*k*0.04*temp_v*shell.velocity.z*dt
		
		
		
		#	重复炮弹的模拟打击，并将爆炸能击中目标的炮弹的初始速度记录下来
		if len(theta_right) > 100:
			print theta_right
			break
		else:
			if shell.pos.y <= -10:
				if (shell.pos.x-target_x)**2+(shell.pos.z-target_z)**2 <= (blast_radius+target_radius)**2:
					theta_right.append(temp_theta)
					shell.color = color.black
				temp_boom = cylinder(pos=(shell.pos.x, shell.pos.y, shell.pos.z), axis=(0, 0.1, 0), color=color.blue,radius=3,opacity=1)
				if theta <= 90:
					temp_theta += 100*dt
					shell = sphere(pos=(0,-10,0), radius=0.5, color=color.yellow)
					theta = get_random(temp_theta,0.01)
					shell.velocity = vector(0, 0, 0)
					v = get_random(input_v, input_unc)
					shell.velocity.x = v*math.cos(theta/180*math.pi)*target_x/math.sqrt(target_x**2+target_z**2)
					shell.velocity.y = v*math.sin(theta/180*math.pi)
					shell.velocity.z = v*math.cos(theta/180*math.pi)*target_z/math.sqrt(target_x**2+target_z**2)
				else:
					print theta_right
					break
		i=i+1