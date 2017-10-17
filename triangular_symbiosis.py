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
t="black"

def line(a,b,c,d):
    plt.plot([a,b],[c,d],color=t)
    
xc=[]
yc=[]
for i in range(100):
    x=100*np.cos(2*i*(np.pi/99))
    y=100*np.sin(2*i*(np.pi/99))
    xc.append(x)
    yc.append(y)
for i in range(75):
    line(xc[i],xc[25+i],yc[i],yc[25+i])
    
for i in range(24):
    line(xc[75+i],xc[1+i],yc[75+i],yc[1+i])
    
for i in range(99):
    line(xc[i],xc[i+1],yc[i],yc[1+i])



line(0,175,200,-100)
line(0,-175,200,-100)
line(-175,175,-100,-100)


for i in range(44):
    line(-87.5-(2*i-0.5),-175+(4*i-0.5),(12/7)*(-87.5-(2*i-0.5))+200,-100)

    line(87.5+(2*i-0.5),175-(4*i+0.5),(-12/7)*(87.5+(2*i-0.5))+200,-100)

    line(-87.5+(2*i-0.5),0+(2*i-0.5),(12/7)*(-87.5+(2*i-0.5))+200,(-12/7)*((2*i-0.5))+200)


frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
frame1.axis('off')	   
savefig('circle_square.png', dpi=300,bbox_inches='tight',pad_inches=0,facecolor="white")