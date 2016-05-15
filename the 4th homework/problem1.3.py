# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def myVelocity(t,v,x,n):
	a=[]
	for i in range(len(t)):
		v_temp=v
		a.append(v)
		v=v_temp+(10.0-v)*x/n	#parameter b=10,a=1
	return a
	
def f(v0,n,x):
	t = np.arange(0.0,x,x/n)
	plt.ylim(0,v0*1.08)			#set the length of yAxis
	plt.plot(t,myVelocity(t,v0,x,n),'bo',t,myVelocity(t,v0,x,n),'k')
	plt.title('$Problem1.3$',fontsize=28)
	plt.xlabel('$t$',fontsize=20)
	plt.ylabel('$V(t)$',fontsize=20)
	plt.show()
	
f(50,100,10.0)  #set v0 and accuracy(the bigger the more accurate) and length of xAxis
