#!/usr/bin/env python
# Na podstawie "Symulacje Komputerowe w Fizyce" prof. Piotra Szymczaka
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.patches import Circle
import matplotlib.animation as animation
G=66.7408 # 10^12 razy wiecej niz w jedn. SI, masy trzeba podawac w 10^12 kg
M=1989000000000000000 # w milionach kg
n=4 # liczba planet
colors=['g', 'm', 'c', 'r', 'm', 'y', 'b', 'g']
m=[328500000000,4867000000000,5972200000000,639000000000,1898000000000000,568000000000000,868000000000000,102000000000000] # w 10^12 kg
mk=73000000000
dt=86400 # tyle sekund jest w 1 dniu
T=dt*365 # tyle sekund jest w jednym roku
T=T*10
t=0
delay=100
r=[]
r.append(np.array([46000000000,0.0]))
r.append(np.array([107500000000,0.0]))
r.append(np.array([147110000000,0.0]))
rk=np.array([147110000000+363000000,0.0])
rz=rk-r[2]
r.append(np.array([206600000000,0.0]))
r.append(np.array([740500000000,0.0]))
r.append(np.array([1352600000000,0.0]))
r.append(np.array([2741300000000,0.0]))
r.append(np.array([4444500000000,0.0]))

p=[]
p.append(np.array([0.0,m[0]*47900.0]))
p.append(np.array([0.0,m[1]*35000.0]))
p.append(np.array([0.0,m[2]*29800.0])) # 30290.0]))
pk=np.array([0.0,mk*(29800.0+1000.0)]) # 30290.0]))
p.append(np.array([0.0,m[3]*24100.0]))
p.append(np.array([0.0,m[4]*13100.0]))
p.append(np.array([0.0,m[5]*9700.0]))
p.append(np.array([0.0,m[6]*6800.0]))
p.append(np.array([0.0,m[7]*5400.0]))

fig = plt.figure()
fig.canvas.manager.set_window_title("Planety w polu centralnym wg Leapfroga")
#gs = gridspec.GridSpec(2, 1)
#plt1 = fig.add_subplot(gs[0,0])
#plt2 = fig.add_subplot(gs[1,0])

x=[]
y=[]
xk=[]
yk=[]
Ekin=[]
Epot=[]
Etot=[]
v=[]
for k in range(n):
	x.append([])
	y.append([])
	Ekin.append([])
	Epot.append([])
	Etot.append([])
	v.append(p[k]/m[k]+G*M/(np.linalg.norm(r[k])**3)*dt*r[k]/2)
vk=pk/mk+G*M/(np.linalg.norm(rk)**3)*dt*rk/2+G*m[2]/(np.linalg.norm(rz)**3)*dt*rz/2
def animate(i):
	global G
	global M
	global m
	global dt
	global t
	global r
	global p
	global t
	global v
	global x
	global y
	global Ekin
	global Epot
	global Etot
	global mk
	global rk
	global pk
	global vk
	global rz
	global xk
	global yk
	
	for j in range(1):
		t=t+dt
		rz=rk-r[2]
		vk=vk-G*M/(np.linalg.norm(rk)**3)*dt*rk-G*m[2]/(np.linalg.norm(rz)**3)*dt*rz
		rk=rk+vk*dt
		for k in range(n):
			v[k]=v[k]-G*M/(np.linalg.norm(r[k])**3)*dt*r[k]
			r[k]=r[k]+v[k]*dt
			#Ekin[k].append(m[k]*np.dot(v[k],v[k])/2)
			#Epot[k].append(-G*M*m[k]/np.linalg.norm(r[k]))
			#Etot[k].append(m[k]*np.dot(v[k],v[k])/2-G*M*m[k]/np.linalg.norm(r[k]))
		
	for k in range(n):
		x[k].append(r[k][0])
		y[k].append(r[k][1])
	xk.append(rk[0])
	yk.append(rk[1])
	#czasy=np.arange(0.0,t,dt)
	#plt1.clear()
	#for k in range(n):
	#	plt1.plot(czasy,Ekin[k], color="r", linestyle="-", linewidth=2)
	#	plt1.plot(czasy,Epot[k], color="g", linestyle="-", linewidth=2)
	#	plt1.plot(czasy,Etot[k], color="b", linestyle="-", linewidth=2)
	#plt1.set_xlabel("czas",fontsize=20)
	#plt1.set_ylabel("energia",fontsize=20)
	#plt1.set_title("t = "+str(t)+" s")
	#plt1.grid(True)
	#plt1.legend(("$E_{kin}$","$E_{pot}$","$E_{tot}$"))
	#plt.savefig("frog.png", format="png")
	plt2=fig
	plt2.clear()
	#plt2.axis('equal')
	a = plt2.gca() 
	sun = Circle((0.0,0.0), radius=20000000000, color='y')
	a.add_patch(sun)
	for k in range(n):
		a.set_xlim(r[2][0]-600000000, r[2][0]+600000000)
		a.set_ylim(r[2][1]-600000000, r[2][1]+600000000)
		plt.plot(x[k],y[k], color=colors[k], linestyle="-", linewidth=1)
		planet = Circle((r[k][0],r[k][1]), radius=100000000,color=colors[k])
		a.add_patch(planet)
	plt.plot(xk,yk, color='k', linestyle="-", linewidth=1)
	moon = Circle((rk[0],rk[1]), radius=50000000,color='k')
	a.add_patch(moon)
	#plt2.xlabel("x",fontsize=20)
	#plt2.ylabel("y",fontsize=20)
	#plt2.title("Planeta w polu centralnym wg Leapfroga")
	plt.grid(True)
	#plt.savefig("frogxy.png", format="png")

ani = animation.FuncAnimation(fig, animate, interval=delay)
plt.show()
