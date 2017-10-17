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
t="black"
def line(a,b,c,d):
     plt.plot([a,b],[c,d],color=t)
     
line(0,100,0,0)
line(0,0,0,100)
line(0,100,100,300)
line(100,300,300,400)
line(300,400,400,300)
line(400,300,300,200)
line(300,400,200,100)
line(400,300,100,0)
line(100,200,0,200)
line(0,200,100,200)


for i in range(25):
    line(0+4*i,100+4*i,0,8*i)
    line(0,8*i,0+4*i,100+4*i)
    line(200-8*i,4*i,200-4*i,100+8*i)
    line(100+8*i,300+4*i,300+4*i,400-4*i)
    line(400-4*i,300+4*i,300-4*i,200-4*i)
    line(300+4*i,400-4*i,200-4*i,100-4*i)
    
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
axis('off')	
savefig('binary_spontaneity.png', dpi=300,bbox_inches='tight',pad_inches=0,facecolor="white")
