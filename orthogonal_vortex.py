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
import collections
import matplotlib.patches as mpatches


t="black"

y_1=0
y_2=250
y_3=500
x_1=0
x_2=250
x_3=500

for r in range(2):
	plt.plot([x_1,x_3],[y_1,y_1], color=t)
	plt.plot([x_3,x_3],[y_1,y_3], color=t)
	plt.plot([x_3,x_1],[y_3,y_3], color=t)
	plt.plot([x_1,x_1],[y_3,y_1], color=t)
	x_1=(x_1+x_2)/2
	y_1=(y_1+y_2)/2
	y_3=(y_2+y_3)/2
	x_3=(x_2+x_3)/2
	
	
y_1_1=0
y_2_2=250
y_3_3=500
x_1_1=0
x_2_2=250
x_3_3=500

for r in range(2):
	plt.plot([x_1_1,x_2_2],[y_2_2,y_1_1], color=t)
	plt.plot([x_2_2,x_3_3],[y_1_1,y_2_2], color=t)
	plt.plot([x_3_3,x_2_2],[y_2_2,y_3_3], color=t)
	plt.plot([x_2_2,x_1_1],[y_3_3,y_2_2], color=t)

	x_1_1=(x_1_1+x_2_2)/2
	x_3_3=(x_2_2+x_3_3)/2
	y_1_1=(y_1_1+y_2_2)/2
	y_3_3=(y_2_2+y_3_3)/2


for r in range(25):
	plt.plot([0+10*r,0],[0,250-10*r], color=t)

	plt.plot([250-10*r,0],[500,500-10*r], color=t)
	
	plt.plot([250+10*r,500],[500,500-10*r], color=t)
	
	plt.plot([500,500-10*r],[250-10*r,0], color=t)
	
	plt.plot([125+5*r,250],[375+5*r,500-5*r],color=t)
	plt.plot([250+5*r,250],[500-5*r,375+5*r],color=t)

	plt.plot([125+5*r,250],[125-5*r,0+5*r],color=t)
	plt.plot([250,250+5*r],[125-5*r, 0+5*r],color=t)

	plt.plot([0+5*r,125-5*r],[250-5*r,250],color=t)
	plt.plot([125-5*r,0+5*r],[375-5*r,250],color=t)

	plt.plot([375+5*r,500-5*r],[375-5*r,250],color=t)
	plt.plot([500-5*r,375+5*r],[250,125+5*r],color=t) 

	plt.plot([125,125+5*r],[250+5*r,375],color=t)
	plt.plot([125,125+3*r],[375-5*r,250+3*r],color=t)
	plt.plot([125+5*r,250-3*r],[375,375-3*r],color=t)

	plt.plot([125,125+5*r],[250-5*r,125],color=t)
	plt.plot([125+5*r,250-3*r],[125,125+3*r],color=t)
	plt.plot([125,125+3*r],[125+5*r,250-3*r],color=t)

	plt.plot([375,375-5*r],[250-5*r,125],color=t)
	plt.plot([375-5*r,250+3*r],[125,125+3*r],color=t)
	plt.plot([375,375-3*r],[125+5*r,250-3*r],color=t)

	plt.plot([250+5*r,375],[375,375-5*r],color=t)
	plt.plot([375,375-3*r],[375-5*r,250+3*r],color=t)
	plt.plot([375-5*r,250+3*r],[375,375-3*r],color=t)



	plt.plot([125+5*r,250],[250,250+5*r],color=t)
	plt.plot([250,250+5*r],[375-5*r,250],color=t)
	plt.plot([250,250+5*r],[125+5*r,250],color=t)
	plt.plot([250,250-5*r],[125+5*r,250],color=t)
    
plt.plot([500,375],[250,250],color=t)
plt.plot([500,250],[250,250],color=t)

xlim(-1,501)
ylim(-1,501)

frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
frame1.axis('off')	
savefig('orthogonal_vortex.png', dpi=300,bbox_inches='tight',pad_inches=0,facecolor="midnightblue")	



