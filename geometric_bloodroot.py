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

x_s=[]
y_s=[]
color_line="blacK"
for i in range(8):
    x=100*cos(i*(np.pi)/4)
    y=100*sin(i*(np.pi)/4)
    x_s.append(x)
    y_s.append(y)
    
slope1=((100-y_s[5])/(0-x_s[5]))
slope2=((y_s[3]-y_s[0])/(x_s[3]-x_s[0]))
leaf1_left_x=(slope1*x_s[5]-slope2*x_s[3]+y_s[3]-y_s[5])/(slope1-slope2)
leaf1_left_y=slope1*(leaf1_left_x-x_s[5])+y_s[5]

slope3=((100-y_s[7])/(0-x_s[7]))
slope4=((y_s[1]-y_s[4])/(x_s[1]-x_s[4]))
leaf1_right_x=(-slope4*x_s[1]+y_s[1]-100)/(slope3-slope4)
leaf1_right_y=leaf1_right_x*slope3+100
plt.plot([0,leaf1_left_x],[0,leaf1_left_y], color=color_line)
plt.plot([0,leaf1_right_x],[0,leaf1_right_y], color=color_line)

slope5=(y_s[3]-y_s[0])/(x_s[3]-x_s[0])
slope6=(y_s[1]-y_s[6])/(x_s[1]-x_s[6])
leaf2_right_x=(-100+100*slope5)/(slope5-slope6)
leaf2_right_y=slope5*(leaf2_right_x-100)

slope7=(y_s[2]-y_s[7])/(x_s[2]-x_s[7])
slope8=(y_s[0]-y_s[5])/(x_s[0]-x_s[5])
leaf3_right_x=(-100*slope8-100)/(slope7-slope8)
leaf3_right_y=slope8*(leaf3_right_x-100)

slope9=(y_s[1]-y_s[6])/(x_s[1]-x_s[6])
slope10=(y_s[7]-y_s[4])/(x_s[7]-x_s[4])
leaf4_right_x=(100*slope10+100)/(slope9-slope10)
leaf4_right_y=slope10*(leaf4_right_x+100)

slope11=(y_s[0]-y_s[5])/(x_s[0]-x_s[5])
slope12=(y_s[6]-y_s[3])/(x_s[6]-x_s[3])
leaf5_right_x=(-100+100*slope11)/(slope11-slope12)
leaf5_right_y=slope11*(leaf5_right_x-100)

slope13=(y_s[2]-y_s[5])/(x_s[2]-x_s[5])
slope14=(y_s[4]-y_s[7])/(x_s[4]-x_s[7])
leaf6_right_x=(slope13*x_s[2]-y_s[2]-slope14*x_s[4]+y_s[4])/(slope13-slope14)
leaf6_right_y=slope13*(leaf6_right_x-x_s[2])+y_s[2]

slope15=(y_s[3]-y_s[6])/(x_s[3]-x_s[6])
slope16=(y_s[1]-y_s[4])/(x_s[1]-x_s[4])
leaf7_right_x=(100*slope16+100)/(slope15-slope16)
leaf7_right_y=slope16*(leaf7_right_x+100)


plt.plot([x_s[1],leaf1_right_x],[y_s[1],leaf1_right_y],color=color_line)
plt.plot([x_s[1],leaf2_right_x],[y_s[1],leaf2_right_y],color=color_line)
plt.plot([x_s[0],leaf2_right_x],[y_s[0],leaf2_right_y],color=color_line)

plt.plot([x_s[0],leaf3_right_x],[y_s[0],leaf3_right_y],color=color_line)
plt.plot([x_s[7],leaf3_right_x],[y_s[7],leaf3_right_y],color=color_line)

plt.plot([x_s[7],leaf4_right_x],[y_s[7],leaf4_right_y],color=color_line)
plt.plot([x_s[6],leaf4_right_x],[y_s[6],leaf4_right_y],color=color_line)

plt.plot([x_s[6],leaf5_right_x],[y_s[6],leaf5_right_y],color=color_line)
plt.plot([x_s[5],leaf5_right_x],[y_s[5],leaf5_right_y],color=color_line)

plt.plot([x_s[5],leaf6_right_x],[y_s[5],leaf6_right_y],color=color_line)
plt.plot([x_s[4],leaf6_right_x],[y_s[4],leaf6_right_y],color=color_line)

plt.plot([x_s[4],leaf7_right_x],[y_s[4],leaf7_right_y],color=color_line)
plt.plot([x_s[3],leaf7_right_x],[y_s[3],leaf7_right_y],color=color_line)

plt.plot([x_s[3],leaf1_left_x],[y_s[3],leaf1_left_y],color=color_line)
for i in range(10):
    plt.plot([0+i*(leaf1_left_x)/10,leaf1_left_x-i*(leaf1_left_x)/10],[100-i*(leaf1_left_y)/10,leaf1_left_y-i*(leaf1_left_y)/10],color=color_line)
    plt.plot([0+i*(leaf1_right_x)/10,leaf1_right_x-i*(leaf1_right_x)/10],[100-i*(leaf1_right_y)/10,leaf1_right_y-i*(leaf1_right_y)/10],color=color_line)

    x1=0+i*(leaf1_right_x)/10
    x2=leaf1_right_x+i*(x_s[1]-leaf1_right_x)/10
    y1=0+i*(leaf1_right_y)/10
    y2=leaf1_right_y+i*(y_s[1]-leaf1_right_y)/10
    plt.plot([x1,x2],[y1,y2],color=color_line)
    
    x3=0+i*(leaf2_right_x)/10
    x4=leaf2_right_x+i*(x_s[1]-leaf2_right_x)/10
    y3=i*(leaf2_right_y)/10
    y4=leaf2_right_y+i*(y_s[1]-leaf2_right_y)/10
    plt.plot([x3,x4],[y3,y4],color=color_line)
    
    x5=0+i*(leaf2_right_x)/10
    x6=leaf2_right_x+i*(100-leaf2_right_x)/10
    y5=0+i*(leaf2_right_y)/10
    y6=leaf2_right_y+i*(0-leaf2_right_y)/10
    plt.plot([x5,x6],[y5,y6],color=color_line)
    
    x7=0+i*(leaf3_right_x)/10
    x8=leaf3_right_x+i*(100-leaf3_right_x)/10
    y7=0+i*(leaf3_right_y)/10
    y8=leaf3_right_y+i*(0-leaf3_right_y)/10
    plt.plot([x7,x8],[y7,y8],color=color_line)
    
    x9=0+i*(leaf3_right_x)/10
    x10=leaf3_right_x+i*(x_s[7]-leaf3_right_x)/10
    y9=0+i*(leaf3_right_y)/10
    y10=leaf3_right_y+i*(y_s[7]-leaf3_right_y)/10
    plt.plot([x9,x10],[y9,y10],color=color_line)
    
    x11=0+i*(leaf4_right_x)/10
    x12=leaf4_right_x+i*(x_s[7]-leaf4_right_x)/10
    y11=0+i*(leaf4_right_y)/10
    y12=leaf4_right_y+i*(y_s[7]-leaf4_right_y)/10
    plt.plot([x11,x12],[y11,y12],color=color_line)
    
    x13=0+i*(leaf4_right_x)/10
    x14=leaf4_right_x+i*(0-leaf4_right_x)/10
    y13=0+i*(leaf4_right_y)/10
    y14=leaf4_right_y+i*(-100-leaf4_right_y)/10
    plt.plot([x13,x14],[y13,y14],color=color_line)
    
    x15=0+i*(leaf5_right_x)/10
    x16=leaf5_right_x+i*(0-leaf5_right_x)/10
    y15=0+i*(leaf5_right_y)/10
    y16=leaf5_right_y+i*(-100-leaf5_right_y)/10
    plt.plot([x15,x16],[y15,y16],color=color_line)
    
    x17=0+i*(leaf5_right_x)/10
    x18=leaf5_right_x+i*(x_s[5]-leaf5_right_x)/10
    y17=0+i*(leaf5_right_y)/10
    y18=leaf5_right_y+i*(y_s[5]-leaf5_right_y)/10
    plt.plot([x17,x18],[y17,y18],color=color_line)
    
    x19=0+i*(leaf6_right_x)/10
    x20=leaf6_right_x+i*(x_s[5]-leaf6_right_x)/10
    y19=0+i*(leaf6_right_y)/10
    y20=leaf6_right_y+i*(y_s[5]-leaf6_right_y)/10
    plt.plot([x19,x20],[y19,y20],color=color_line)
    
    x21=0+i*(leaf6_right_x)/10
    x22=leaf6_right_x+i*(-100-leaf6_right_x)/10
    y21=0+i*(leaf6_right_y)/10
    y22=leaf6_right_y+i*(0-leaf6_right_y)/10
    plt.plot([x21,x22],[y21,y22],color=color_line)
    
    
    x23=0+i*(leaf7_right_x)/10
    x24=leaf7_right_x+i*(-100-leaf7_right_x)/10
    y23=0+i*(leaf7_right_y)/10
    y24=leaf7_right_y+i*(0-leaf7_right_y)/10
    plt.plot([x23,x24],[y23,y24],color=color_line)
    
    x25=0+i*(leaf7_right_x)/10
    x26=leaf7_right_x+i*(x_s[3]-leaf7_right_x)/10
    y25=0+i*(leaf7_right_y)/10
    y26=leaf7_right_y+i*(y_s[3]-leaf7_right_y)/10
    plt.plot([x25,x26],[y25,y26],color=color_line)
    
    x27=0+i*(leaf1_left_x)/10
    x28=leaf1_left_x+i*(x_s[3]-leaf1_left_x)/10
    y27=0+i*(leaf1_left_y)/10
    y28=leaf1_left_y+i*(y_s[3]-leaf1_left_y)/10
    plt.plot([x27,x28],[y27,y28],color=color_line)
  
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
frame1.axis('off')	
savefig('geometric_bloodroot.png', dpi=300, bbox_inches='tight',pad_inches=0,facecolor="white")
	    
    
    
