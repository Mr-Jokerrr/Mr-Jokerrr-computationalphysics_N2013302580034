# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8
l1 = 0.5
l2 = 1.0
l3 = 1.5
l4 = 2.0
ini_x = 1.5
ini_v = 0
ini_a = 0
dt = 0.001
t = np.arange(0,10,dt)
p1 = []
p2 = []
p3 = []
p4 = []

x = ini_x
v = ini_v
a = ini_a
for i in range(len(t)):
	p1.append(x)
	a = - g/l1*math.sin(x)
	v += a*dt
	x += v*dt

x = ini_x
v = ini_v
a = ini_a
for i in range(len(t)):
	p2.append(x)
	a = - g/l2*math.sin(x)
	v += a*dt
	x += v*dt

x = ini_x
v = ini_v
a = ini_a
for i in range(len(t)):
	p3.append(x)
	a = - g/l3*math.sin(x)
	v += a*dt
	x += v*dt

x = ini_x
v = ini_v
a = ini_a
for i in range(len(t)):
	p4.append(x)
	a = - g/l4*math.sin(x)
	v += a*dt
	x += v*dt

plt.plot(t,p1,'b',t,p2,'r',t,p3,'k',t,p4,'g')
plt.text(7.6,1.8,u'nonlinear pendulum',color='black',ha='center',fontsize=16)
plt.text(7.6,1.7,u'l=0.5,g=9.8',color='blue',ha='center',fontsize=16)
plt.text(7.6,1.6,u'l=1.0,g=9.8',color='red',ha='center',fontsize=16)
plt.text(7.6,1.5,u'l=1.5,g=9.8',color='black',ha='center',fontsize=16)
plt.text(7.6,1.4,u'l=2.0,g=9.8',color='green',ha='center',fontsize=16)
plt.title('$Problem3.8$',fontsize=28)
plt.xlabel('$time(s)$',fontsize=20)
plt.ylabel(u'$\u03B8(radians)$',fontsize=20)
plt.show()
