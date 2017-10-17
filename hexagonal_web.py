from math import *
from sympy import *
import random
from mpmath import *
import fractions
from fractions import *
import sympy
import math
import sys
from random import *
import json
sys.modules['sympy.mpmath'] = mpmath
import matplotlib
from matplotlib import *
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import pylab
import itertools
from itertools import *
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from sympy.simplify.fu import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def dl(a,b,c,d):
	plt.plot([a,b],[c,d],color=t)

t="black"

x=[]
y=[]

for i in range(7):
	xc=400*cos(2.0*(i*np.pi/6))
	yc=400*sin(2.0*(i*np.pi/6))
	x.append(xc)
	y.append(yc)


dl(0,0,-340/2,340/2)
 
dl(-150,150, (-340)/4, (340)/4)
dl(150,-150,(-340)/4, (340)/4)
a=340/2.0
slope=((-340)/4-(340)/4)/(-150.0-150)
slope2=(((-340)/4)-((340)/4))/(150-(-150))

i=0
b=85

side1x=[]
side1y=[]
side2x=[]
side2y=[]
side3x=[]
side3y=[]
side4x=[]
side4y=[]
while(i<=170):
	
	dl(0,0-i,a-i,0+slope*i)
	
	dl(0,0+i,a-i,0+slope*i)
	
	dl(0,0-i,-a+i,0-slope*i)
	dl(0,0+i,-a+i,0-slope*i)
	sx1=0+i
	sy1=slope*i
	sx2=0+i
	sy2=-slope*i
	
	sx3=0-i
	sy3=slope*i
	sx4=0-i
	sy4=-slope*i
	
	side1x.append(sx1)
	side2x.append(sx2)
	side1y.append(sy1)
	side2y.append(sy2)
	side3x.append(sx3)
	side3y.append(sy3)
	side4x.append(sx4)
	side4y.append(sy4)

	i=i+17
	
m=len(side1x)-1
for i in range(len(side1x)):
	plt.plot([side1x[m], side2x[i]], [side1y[m],side2y[i]], color=t)
	plt.plot([side3x[m], side4x[i]], [side3y[m],side4y[i]], color=t)
	m=m-1

dl(x[0],side1x[-1],y[0],side1y[-1])
dl(x[1],side1x[-1],y[1],side1y[-1])

dl(x[2],0, y[2], 170)
dl(x[1],0, y[1],170)

dl(x[2],side3x[-1],y[2],side3y[-1])
dl(x[3], side3x[-1], y[3], side3y[-1])
dl(x[3], side4x[-1], y[3], side4y[-1])
dl(x[4], side4x[-1], y[4], side4y[-1])

dl(x[4], 0, y[4], -170)
dl(x[5], 0, y[5], -170)

dl(x[5], side2x[-1], y[5], side2y[-1])
dl(x[0], side2x[-1], y[0], side2y[-1])

slope4=(-170-y[5])/(0-x[5])
slope5=(y[5]-side2y[-1])/(x[5]-side2x[-1])

slope6=(y[0]-side2y[-1])/(x[0]-side2x[-1])
slope7=(y[0]-side1y[-1])/(x[0]-side1x[-1])

slope8=(y[1]-side1y[-1])/(x[1]-side1x[-1])
slope9=(y[1]-170)/(x[1]-0)

slope10=(y[2]-170)/(x[2]-0)
slope11=(y[2]-side3y[-1])/(x[2]-side3x[-1])

slope12=(y[3]-side3y[-1])/(x[3]-side3x[-1])
slope13=(y[3]-side4y[-1])/(x[3]-side4x[-1])

slope14=(side4y[-1]-y[4])/(side4x[-1]-x[4])
slope15=(y[4]-(-170))/(x[4]-0)

newslope1=(side3y[-1]-y[3])/(side3x[-1]-x[3])
newslope2=(y[3]-side4y[-1])/(x[3]-side4x[-1])

i=0
g=0
while(i<=100):
	dl(0+2*i,x[5]-g,-170+slope4*2*i, y[5]-slope5*g)
	
	dl(side1x[-1]+2*i,x[0]-2*i,side1y[-1]-slope6*2*i, y[0]+slope7*2*i)
	
	dl(0+2*i,x[1]-g,170+slope9*2*i,y[1]-slope8*g)
	
	dl(0-2*i, x[2]+g,170-slope10*2*i,y[2]+slope11*g)
	
	dl(side4x[-1]-g,x[4]+2*i,side4y[-1]-slope14*g,y[4]+slope15*2*i)
	
	i=i+10
	g=g+3

i=0
g=0
lastx=[]
lastx2=[]
lasty=[]
lasty2=[]
while(i<=100):
	plt.plot([x[2]+2*i,0+2*i],[y[2]-slope9*2*i,170+slope9*2*i], color="black")
	plt.plot([x[4]+2*i,0+2*i],[y[4]+slope9*2*i,-170-slope9*2*i], color="black")
	
	dl(x[1]-g,side1x[-1]+2*i,y[1]-slope14*g,side1y[-1]-slope6*2*i)
	dl(x[0]-2*i,side2x[-1]+g,y[0]-slope6*2*i,side2y[-1]-slope14*g)
	dl(x[4]+g,side4x[-1]-2*i,y[4]+slope14*g,side4y[-1]+slope12*2*i)
	dl(x[3]+2*i,side3x[-1]-g,y[3]+2*i*slope12,side3y[-1]+slope14*g)
	
	lastx.append(x[3]+2*i)
	lasty.append(y[3]+2*i*slope12)
	lastx2.append(side4x[-1]-2*i)
	lasty2.append(side4y[-1]+slope12*2*i)
	
	i=i+10
	g=g+3
	
m=len(lastx)-1
for i in range(len(lastx)):
	dl(lastx[i],lastx2[i],lasty[i],lasty2[i])
	m=m-1


pslope1=(170-side3y[-1])/(0-side3x[-1])
pslope2=(170-side1y[-1])/(0-side1x[-1])

frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
frame1.axis('off')
savefig('hexagonal_web.png', dpi=300, bbox_inches='tight',pad_inches=0, facecolor="white")		
		