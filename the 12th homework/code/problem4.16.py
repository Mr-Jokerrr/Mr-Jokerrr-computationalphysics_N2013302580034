#	-*- coding: utf-8 -*-
from visual import *
import time
import math

#	Get Vmax, k=Mp/Ms
def get_Vmax(a,e,k):
	Vmax = 2*math.pi*math.sqrt((1+e)*(1+k)/a/(1-e))
	return Vmax

#	Get Vmin, k=Mp/Ms
def get_Vmin(a,e,k):
	Vmin = 2*math.pi*math.sqrt((1-e)*(1+k)/a/(1+e))
	return Vmin
	
#	set parameter
R = 0
GMs = 4*(math.pi**2)
GMe = 0.000003*GMs
GMj = 1000*0.00095*GMs
dt = 0.001

#	create two Planets
Pe_ini_x = 1.0*(1-0.017)
Pj_ini_x = 5.2*(1-0.048)
Ps = sphere(pos=(0,0,0), radius=0.5, color=color.yellow)			#Sun
Pe = sphere(pos=(Pe_ini_x,0,0), radius=0.1, color=color.blue)		#Earth
Pj = sphere(pos=(-Pj_ini_x,0,0), radius=0.2, color=color.red)		#Jupiter
ground = box(pos=(0,0,0),length=18,height=18,width=0.1,opacity=0)

Ps.velocity = vector(0, 0, 0)

VPey_ini = get_Vmax(1.0,0.017,0.000003)
Pe.velocity = vector(0, 0, 0)
Pe.velocity.y = VPey_ini

VPjy_ini = get_Vmax(5.2,0.048,0.00095)
Pj.velocity = vector(0, 0, 0)
Pj.velocity.y = -VPjy_ini

while 1:
	rate(1000)
	
	Rse = math.sqrt((Ps.x-Pe.x)**2+(Ps.y-Pe.y)**2)
	Rsj = math.sqrt((Ps.x-Pj.x)**2+(Ps.y-Pj.y)**2)
	Rej = math.sqrt((Pe.x-Pj.x)**2+(Pe.y-Pj.y)**2)
	
	aPsx = GMe*(Pe.x-Ps.x)/(Rse**3)+GMj*(Pj.x-Ps.x)/(Rsj**3)
	aPsy = GMe*(Pe.y-Ps.y)/(Rse**3)+GMj*(Pj.y-Ps.y)/(Rsj**3)
	aPex = GMs*(Ps.x-Pe.x)/(Rse**3)+GMj*(Pj.x-Pe.x)/(Rej**3)
	aPey = GMs*(Ps.y-Pe.y)/(Rse**3)+GMj*(Pj.y-Pe.y)/(Rej**3)
	aPjx = GMs*(Ps.x-Pj.x)/(Rsj**3)+GMe*(Pe.x-Pj.x)/(Rej**3)
	aPjy = GMs*(Ps.y-Pj.y)/(Rsj**3)+GMe*(Pe.y-Pj.y)/(Rej**3)
	
	Ps.velocity.x += aPsx*dt
	Ps.velocity.y += aPsy*dt
	Pe.velocity.x += aPex*dt
	Pe.velocity.y += aPey*dt
	Pj.velocity.x += aPjx*dt
	Pj.velocity.y += aPjy*dt

	Ps.pos += Ps.velocity*dt
	Pe.pos += Pe.velocity*dt
	Pj.pos += Pj.velocity*dt
