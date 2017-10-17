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
plt.plot([0,500],[0,0], color=t)
plt.plot([0,0],[0,500], color=t)
plt.plot([0,250],[500,500], color=t)
plt.plot([250,250],[500,250], color=t)
plt.plot([250,500],[250,250], color=t)
plt.plot([500,500],[250,0], color=t)



for i in range(25):
    plt.plot([0,0+10*i],[250-10*i,0],color=t)
    plt.plot([250+10*i,500],[0,0+10*i],color=t)
    plt.plot([250+10*i,500],[250,250-10*i],color=t)
    
    
    plt.plot([0+10*i,250],[500,500-10*i],color=t)
    plt.plot([0,0+10*i],[250+10*i,500],color=t)
    plt.plot([250,250+10*i],[500-10*i,250],color=t)
    
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
frame1.axis('off')	

savefig('concave_captivation.png', dpi=300, bbox_inches='tight',pad_inches=0, facecolor="goldenrod")	











