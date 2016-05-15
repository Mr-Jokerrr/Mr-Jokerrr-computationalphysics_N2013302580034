# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def myN(t,mN,x,n,a,b):
	p=[]
	for i in range(len(t)):
		mN_temp=mN
		p.append(mN)
		mN=mN_temp+(a*mN-b*(mN**2))*x/n
	return p
	
def f(mN0,n,x,a,b):
	t = np.arange(0.0,x,x/n)
	plt.plot(t,myN(t,mN0,x,n,a,b),'bo',t,myN(t,mN0,x,n,a,b),'k')
	plt.title('$Problem1.6$',fontsize=28)
	plt.xlabel('$t$',fontsize=20)
	plt.ylabel('$N(t)$',fontsize=20)
	plt.show()
	
f(3.5,1000,10.0,10,3)  #set v0 and accuracy(the bigger the more accurate) and length of xAxis and the parameter of a,b
