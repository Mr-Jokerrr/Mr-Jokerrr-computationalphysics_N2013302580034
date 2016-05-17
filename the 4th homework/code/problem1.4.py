# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def myA(t,mA,mB,x,n,a,b):
	p=[]
	q=[]
	for i in range(len(t)):
		mA_temp=mA
		mB_temp=mB
		p.append(mA)
		q.append(mB)
		mA=mA_temp-(mA_temp/a)*x/n
		mB=mB_temp+((mA_temp/a)-(mB_temp/b))*x/n
	return p

def myB(t,mA,mB,x,n,a,b):
	p=[]
	q=[]
	for i in range(len(t)):
		mA_temp=mA
		mB_temp=mB
		p.append(mA)
		q.append(mB)
		mA=mA_temp-(mA_temp/a)*x/n
		mB=mB_temp+((mA_temp/a)-(mB_temp/b))*x/n
	return q

def main(mA0,mB0,n,x,a,b):
	t = np.arange(0.0,x,x/n)
	plt.plot(t,myA(t,mA0,mB0,x,n,a,b),'bo',t,myA(t,mA0,mB0,x,n,a,b),'k',t,myB(t,mA0,mB0,x,n,a,b),'bo',t,myB(t,mA0,mB0,x,n,a,b),'k')
	plt.title('$Problem1.4$',fontsize=28)
	plt.xlabel('$t$',fontsize=20)
	plt.ylabel('$N$',fontsize=20)
	plt.show()

main(3.5,3.5,1000,10.0,10,3)  #set mA0,mB0 and accuracy(the bigger the more accurate) and length of xAxis and the parameter of a,b
