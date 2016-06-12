# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

def reduce_theta(x):
	if x > math.pi:
		return reduce_theta(x - 2*math.pi)
	elif x < -math.pi:
		return reduce_theta(x + 2*math.pi)
	else:
		return x

#	set parameter
dt = 0.0001
GMsat = 4*(math.pi**2)

xc = 1.0
yc = 0
vxc = 0
vyc = 5.0
theta1 = 0
omega1 = 0
theta2 = 0.01
omega2 = 0
dtheta = 0
t = 0

#theta1_array = []
#theta2_array = []
dtheta_array = []
#omega_array = []
t_array = []
xc_array = []
yc_array = []

while t<=10:
	dtheta_array.append(dtheta)
	#theta1_array.append(theta1)
	#theta2_array.append(theta2)
	#omega_array.append(omega1)
	t_array.append(t)
	xc_array.append(xc)
	yc_array.append(yc)
	
	r = math.sqrt(xc**2+yc**2)
	
	vxc += -GMsat*xc*dt/r**3
	vyc += -GMsat*yc*dt/r**3
	xc += vxc*dt
	yc += vyc*dt
	
	omega1 += dt*(-3*GMsat*(xc*math.sin(theta1)-yc*math.cos(theta1))*(xc*math.cos(theta1)+yc*math.sin(theta1))/r**5)
	omega2 += dt*(-3*GMsat*(xc*math.sin(theta2)-yc*math.cos(theta2))*(xc*math.cos(theta2)+yc*math.sin(theta2))/r**5)

	theta1 += omega1*dt
	theta2 += omega2*dt
	#theta1 = reduce_theta(theta1)
	#theta2 = reduce_theta(theta2)
	
	dtheta = abs(theta1-theta2)
	
	t += dt

plt.plot(t_array,dtheta_array,'-k')
plt.title('$Problem4.20$',fontsize=28)
plt.xlabel('time(yr)',fontsize=20)
plt.ylabel(u'$\u03B8$(radians)',fontsize=20)
#plt.text(1,14,'r=10',color='black',ha='center',fontsize=20)
plt.show()