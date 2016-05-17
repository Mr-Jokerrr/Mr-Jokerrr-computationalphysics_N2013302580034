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
	

#	设置基本参数
dt = 0.01
dAngle = 3					#	每次变化的角度，角度越小精度越高，计算速度越慢
earth_spinv = math.pi/720	#	自转角速度
	

#	设置其他参数
earth_r = 50				#	地球半径
missile_v = 1800000*earth_r/6371/1000			#	导弹发射初始速度,定为30km每秒，即1800km每分钟
missile_latitude = 30		#	导弹发射初始纬度，正代表北纬
missile_longitude = 113.5	#	导弹发射初始经度，正代表东经
blast_radius = 3			#	导弹爆炸半径

missile_alpha = 0			#	导弹发射仰角，0°-90°
missile_beta = 0			#	导弹发射地面角，指向南极为0°，向目标方向转动，指向北极为180°

target_radius = 1			#	目标半径
target_latitude = 35.5		#	目标初始纬度
target_longitude = 139.5	#	目标初始经度


#	将导弹的初始发射经度固定在40度或者140度,便于观察
if missile_longitude-target_longitude < 0:
	target_longitude -= missile_longitude-40
	missile_longitude =  40
else:
	target_longitude -= missile_longitude-140
	missile_longitude =  140


#	将目标坐标、导弹初始坐标、导弹初始速度转换为直角坐标
target_x = earth_r*math.cos(target_latitude*math.pi/180)*math.cos((180-target_longitude)*math.pi/180)
target_y = earth_r*math.sin(target_latitude*math.pi/180)
target_z = earth_r*math.cos(target_latitude*math.pi/180)*math.sin((180-target_longitude)*math.pi/180)

missile_ini_x = earth_r*math.cos(missile_latitude*math.pi/180)*math.cos((180-missile_longitude)*math.pi/180)
missile_ini_y = earth_r*math.sin(missile_latitude*math.pi/180)
missile_ini_z = earth_r*math.cos(missile_latitude*math.pi/180)*math.sin((180-missile_longitude)*math.pi/180)

missile_ini_vx = missile_v*math.sin(missile_latitude*math.pi/180)*math.cos(missile_alpha*math.pi/180)*math.cos((180-missile_beta)*math.pi/180)+missile_v*math.cos(missile_latitude*math.pi/180)*math.sin(missile_alpha*math.pi/180)
missile_ini_vy = missile_v*math.cos(missile_latitude*math.pi/180)*math.cos(missile_alpha*math.pi/180)*math.cos((180-missile_beta)*math.pi/180)+missile_v*math.sin(missile_latitude*math.pi/180)*math.sin(missile_alpha*math.pi/180)
missile_ini_vz = missile_v*math.sin((180-missile_beta)*math.pi/180)*math.cos(missile_alpha*math.pi/180)



'''
	模拟得到最佳发射仰角及水平角
'''
#	设置初始值
sim_distance=100000
final_alpha=0
final_beta=0
missile_x = missile_ini_x
missile_y = missile_ini_y
missile_z = missile_ini_z
missile_vx = missile_ini_vx
missile_vy = missile_ini_vy
missile_vz = missile_ini_vz


while missile_alpha <= 90:
	#	重复炮弹的模拟打击，每个角度重复十次
	i=0
	temp_sim_distance = 0
	while i<11:
		while missile_x**2+missile_y**2+missile_z**2 > earth_r**2:
			#	导弹飞行轨迹
			temp_v = math.sqrt(missile_vx**2+missile_vy**2+missile_vz**2)
			missile_x += missile_vx*dt
			missile_y += missile_vy*dt
			missile_z += missile_vz*dt
			k = get_random(1,0.1)	#	风阻误差
			H = math.sqrt(missile_x**2+missile_y**2+missile_z**2)-earth_r
			real_H = H / earth_r *(6371*1000)	#	真实的海拔高度
			

			#	科里奥利力引起的加速度
			a_x = math.pi/360*missile_vz
			a_z = -math.pi/360*missile_vx


			#	重力加速度
			g_x = 24564.19264/((H+earth_r)**2)*missile_x/math.sqrt(missile_x**2+missile_y**2+missile_z**2)
			g_y = 24564.19264/((H+earth_r)**2)*missile_y/math.sqrt(missile_x**2+missile_y**2+missile_z**2)
			g_z = 24564.19264/((H+earth_r)**2)*missile_z/math.sqrt(missile_x**2+missile_y**2+missile_z**2)
			
			
			#	速度变化，高度超过一定范围则忽略风阻
			if 0.0065*real_H<288:
				missile_vx -= (1-(0.0065*real_H)/288)**2.5*k*0.04*temp_v*missile_vx*dt + g_x*dt + a_x*dt
				missile_vy -= (1-(0.0065*real_H)/288)**2.5*k*0.04*temp_v*missile_vy*dt + g_y*dt
				missile_vz -= (1-(0.0065*real_H)/288)**2.5*k*0.04*temp_v*missile_vz*dt + g_z*dt + a_z*dt
			else:
				missile_vx -= g_x*dt + a_x*dt
				missile_vy -= g_y*dt
				missile_vz -= g_z*dt + a_z*dt
		temp_sim_distance += (missile_x-target_x)**2+(missile_y-target_y)**2+(missile_z-target_z)**2
		i += 1

	#	如果方差更小，则储存此时的alpha角和beta角
	if temp_sim_distance < sim_distance:
		sim_distance = temp_sim_distance
		final_alpha = missile_alpha
		final_beta = missile_beta
	if missile_beta <= 180:
		missile_beta += dAngle
		missile_x = missile_ini_x
		missile_y = missile_ini_y
		missile_z = missile_ini_z
		missile_vx = missile_v*math.sin(missile_latitude*math.pi/180)*math.cos(missile_alpha*math.pi/180)*math.cos((180-missile_beta)*math.pi/180)+missile_v*math.cos(missile_latitude*math.pi/180)*math.sin(missile_alpha*math.pi/180)
		missile_vy = missile_v*math.cos(missile_latitude*math.pi/180)*math.cos(missile_alpha*math.pi/180)*math.cos((180-missile_beta)*math.pi/180)+missile_v*math.sin(missile_latitude*math.pi/180)*math.sin(missile_alpha*math.pi/180)
		missile_vz = missile_v*math.sin((180-missile_beta)*math.pi/180)*math.cos(missile_alpha*math.pi/180)
	else: 
		missile_alpha += dAngle
		missile_beta = 0
print "alpha", missile_alpha
print "beta", missile_beta

	
	
'''
	在VPthon上模拟发射
'''
#	得到最优发射角
missile_alpha = final_alpha
missile_beta = final_beta


#	将目标坐标、导弹初始坐标、导弹初始速度转换为直角坐标
target_x = earth_r*math.cos(target_latitude*math.pi/180)*math.cos((180-target_longitude)*math.pi/180)
target_y = earth_r*math.sin(target_latitude*math.pi/180)
target_z = earth_r*math.cos(target_latitude*math.pi/180)*math.sin((180-target_longitude)*math.pi/180)

missile_ini_x = earth_r*math.cos(missile_latitude*math.pi/180)*math.cos((180-missile_longitude)*math.pi/180)
missile_ini_y = earth_r*math.sin(missile_latitude*math.pi/180)
missile_ini_z = earth_r*math.cos(missile_latitude*math.pi/180)*math.sin((180-missile_longitude)*math.pi/180)

missile_ini_vx = missile_v*math.sin(missile_latitude*math.pi/180)*math.cos(missile_alpha*math.pi/180)*math.cos((180-missile_beta)*math.pi/180)+missile_v*math.cos(missile_latitude*math.pi/180)*math.sin(missile_alpha*math.pi/180)
missile_ini_vy = missile_v*math.cos(missile_latitude*math.pi/180)*math.cos(missile_alpha*math.pi/180)*math.cos((180-missile_beta)*math.pi/180)+missile_v*math.sin(missile_latitude*math.pi/180)*math.sin(missile_alpha*math.pi/180)
missile_ini_vz = missile_v*math.sin((180-missile_beta)*math.pi/180)*math.cos(missile_alpha*math.pi/180)


#	创建导弹、地面、目标的VPython图形
missile = sphere(pos=(missile_ini_x,missile_ini_y,missile_ini_z), radius=1, color=color.yellow)
earth = sphere(pos=(0,0,0), radius=earth_r, color=color.white, opacity = 0.7)
target = sphere(pos=(target_x, target_y, target_z), radius=target_radius, color=color.red)

missile.velocity = vector(0, 0, 0)
missile.velocity.x = missile_ini_vx
missile.velocity.y = missile_ini_vy
missile.velocity.z = missile_ini_vz

missile.pos.x = missile_ini_x
missile.pos.y = missile_ini_y
missile.pos.z = missile_ini_z


while 1:
	#	设置动画速度
	rate(100)

	
	#	导弹飞行轨迹
	temp_v = math.sqrt(missile.velocity.x**2+missile.velocity.y**2+missile.velocity.z**2)
	missile.pos += missile.velocity*dt
	k = get_random(1,0.1)	#	风阻误差
	H = math.sqrt(missile.pos.x**2+missile.pos.y**2+missile.pos.z**2)-earth_r
	real_H = H / earth_r *(6371*1000)	#	真实的海拔高度
	

	#	科里奥利力引起的加速度
	a_x = math.pi/360*missile.velocity.z
	a_z = -math.pi/360*missile.velocity.x


	#	重力加速度
	g_x = 24564.19264/((H+earth_r)**2)*missile.pos.x/math.sqrt(missile.pos.x**2+missile.pos.y**2+missile.pos.z**2)
	g_y = 24564.19264/((H+earth_r)**2)*missile.pos.y/math.sqrt(missile.pos.x**2+missile.pos.y**2+missile.pos.z**2)
	g_z = 24564.19264/((H+earth_r)**2)*missile.pos.z/math.sqrt(missile.pos.x**2+missile.pos.y**2+missile.pos.z**2)
	
	
	#	速度变化，高度超过一定范围则忽略风阻
	if 0.0065*real_H<288:
		missile.velocity.x -= (1-(0.0065*real_H)/288)**2.5*k*0.04*temp_v*missile.velocity.x*dt + g_x*dt + a_x*dt
		missile.velocity.y -= (1-(0.0065*real_H)/288)**2.5*k*0.04*temp_v*missile.velocity.y*dt + g_y*dt
		missile.velocity.z -= (1-(0.0065*real_H)/288)**2.5*k*0.04*temp_v*missile.velocity.z*dt + g_z*dt + a_z*dt
	else:
		missile.velocity.x -= g_x*dt + a_x*dt
		missile.velocity.y -= g_y*dt
		missile.velocity.z -= g_z*dt + a_z*dt
	
	
	#	导弹打到地面即结束模拟
	if missile.pos.x**2+missile.pos.y**2+missile.pos.z**2 <= earth_r**2:
		missile.color = color.black
		r = sqrt(missile.pos.x**2+missile.pos.y**2+missile.pos.z**2)
		temp_boom = cylinder(pos=(missile.pos.x, missile.pos.y, missile.pos.z), axis=(0.05*missile.pos.x/r, 0.05*missile.pos.y/r, 0.05*missile.pos.z/r), color=color.blue,radius=3,opacity=0.4)
		break
