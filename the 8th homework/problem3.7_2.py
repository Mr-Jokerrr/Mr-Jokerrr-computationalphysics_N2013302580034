# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8
l = 1.0
oumiga = 2.0
fd = 0.2
q1 = 0.5
q2 = 1.0
q3 = 2.0
q4 = 3.0
ini_x = 0.2
v = 0
a = 0
dt = 0.001
t = np.arange(0,25,dt)
p1 = []
p2 = []
p3 = []
p4 = []

x = ini_x
for i in range(len(t)):
	p1.append(x)
	a = - g/l*x - q1*v + fd*math.sin(oumiga*t[i])
	v += a*dt
	x += v*dt
	
x = ini_x
for i in range(len(t)):
	p2.append(x)
	a = - g/l*x - q2*v + fd*math.sin(oumiga*t[i])
	v += a*dt
	x += v*dt	
	
x = ini_x
for i in range(len(t)):
	p3.append(x)
	a = - g/l*x - q3*v + fd*math.sin(oumiga*t[i])
	v += a*dt
	x += v*dt
	
x = ini_x
for i in range(len(t)):
	p4.append(x)
	a = - g/l*x - q4*v + fd*math.sin(oumiga*t[i])
	v += a*dt
	x += v*dt
	
plt.plot(t,p1,'b',t,p2,'r',t,p3,'k',t,p4,'g')
plt.text(15,0.18,u'driven pendulum',color='black',ha='center',fontsize=16)
plt.text(15,0.16,u'\u03A9=2.0, F=0.2, q=0.5',color='blue',ha='center',fontsize=16)
plt.text(15,0.14,u'\u03A9=2.0, F=0.2, q=1.0',color='red',ha='center',fontsize=16)
plt.text(15,0.12,u'\u03A9=2.0, F=0.2, q=2.0',color='black',ha='center',fontsize=16)
plt.text(15,0.10,u'\u03A9=2.0, F=0.2, q=3.0',color='green',ha='center',fontsize=16)
plt.title('$Problem3.7$',fontsize=28)
plt.xlabel('$time(s)$',fontsize=20)
plt.ylabel(u'$\u03B8(radians)$',fontsize=20)
plt.show()
