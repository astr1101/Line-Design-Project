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
#inside part
i=0
while(i<=50):
	plt.plot([i, 50], [i, 50-i], color=t)
	plt.plot([50, 50+i], [0+i, 50-i], color=t)
	plt.plot([100-i, 50+i], [0+i, 50], color=t)
	plt.plot([100-i, 50+i], [100-i, 50], color=t)
	plt.plot([100-i, 50], [100-i, 50+i], color=t)
	plt.plot([0+i, 50], [100-i, 50+i], color=t)
	plt.plot([0+i, 50-i], [100-i, 50], color=t)
	plt.plot([0+i, 50-i], [0+i, 50], color=t)
	i=i+2.5



i=0
while(i<=25):
	plt.plot([0+i, 25+i], [0-2*i, -50+2*i], color=t)
	plt.plot([50+i, 75+i], [0-2*i, -50+2*i], color=t)
	plt.plot([25+i, 50+i], [-50+2*i, 0-2*i], color=t)
	
	plt.plot([0+i, 25+i], [100+2*i, 150-2*i], color=t)
	plt.plot([50+i, 75+i], [100+2*i, 150-2*i], color=t)
	plt.plot([25+i, 50+i], [150-2*i,100+2*i], color=t)
	
	plt.plot([100+2*i, 150-2*i], [100-i, 75-i], color=t)
	plt.plot([100+2*i, 150-2*i], [50-i, 25-i], color=t)
	plt.plot([150-2*i, 100+2*i], [75-i, 50-i], color=t)
	
	plt.plot([0-2*i, -50+2*i], [100-i, 75-i], color=t)
	plt.plot([0-2*i, -50+2*i], [50-i, 25-i], color=t)
	plt.plot([-50+2*i, 0-2*i], [75-i, 50-i], color=t)
	
	plt.plot([25-i, 0-2*i], [150-2*i, 100-i], color=t)
	plt.plot([75+i, 100+2*i], [150-2*i, 100-i], color=t)
	plt.plot([150-2*i,100-i],[25-i,0-2*i], color=t)
	plt.plot([-50+2*i, 0+i], [25-i,0-2*i], color=t)

	plt.plot([-50, -50+3*i], [25-3*i, -50], color=t)
	plt.plot([150, 150-3*i], [25-3*i, -50], color=t)
	plt.plot([150, 150-3*i], [75+3*i, 150], color=t)
	plt.plot([-50, -50+3*i], [75+3*i, 150], color=t)

	plt.plot([50+i, 75-2*i], [0-2*i, -50], color=t)
	plt.plot([50-i, 25+2*i], [0-2*i, -50], color=t)
	plt.plot([50+i, 75-2*i], [100+2*i, 150], color=t)
	plt.plot([50-i,25+2*i],[100+2*i,150],color=t)

	plt.plot([100+2*i,150],[50-i,25+2*i], color=t)
	plt.plot([100+2*i,150],[50+i,75-2*i],color=t)
	
	plt.plot([0-2*i,-50],[50+i,75-2*i],color=t)
	plt.plot([0-2*i,-50],[50-i,25+2*i],color=t)
	
	i=i+2.5



xlim(-51, 151)
ylim(-51, 151)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
frame1.axis('off')
savefig('octagram_mirage.png', bbox_inches='tight',pad_inches=0, facecolor="white")	
