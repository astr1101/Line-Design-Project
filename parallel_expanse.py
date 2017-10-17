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
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import collections
import matplotlib.patches as mpatches

t="black"

plt.plot([0,50],[0,0], color=t)
plt.plot([0, 0], [0, 50], color=t)
plt.plot([50,50], [0, 50], color=t)
plt.plot([0, 25], [50, 100], color=t)
plt.plot([25,50],[100,50], color=t)
plt.plot([0,50],[0,50], color=t)
plt.plot([50,0],[0,50], color=t)

for i in range(15):
	plt.plot([25-i,10+i],[100-4*i,40-i], color=t)
	plt.plot([25+i,40-i],[100-4*i,40-i], color=t)
	plt.plot([25-i,10-Fraction(10,15)*i],[100-4*i,40+Fraction(10,15)*i], color=t)
	plt.plot([25-Fraction(25,15)*i,0+Fraction(10,15)*i],[100-Fraction(50,15)*i,50-Fraction(10,15)*i], color=t)
	plt.plot([0+Fraction(25,15)*i,25-i],[0+Fraction(25,15)*i,25+i], color=t)
	plt.plot([25-Fraction(25,15)*i,0+Fraction(25,15)*i],[25-Fraction(25,15)*i,0], color=t)
	plt.plot([10-Fraction(10,15)*i,0],[40+Fraction(10,15)*i,50-Fraction(50,15)*i], color=t)
	plt.plot([25+Fraction(25,15)*i,50-Fraction(25,15)*i],[25-Fraction(25,15)*i,0], color=t)
	plt.plot([40-i,25+Fraction(25,15)*i],[40-i,25-Fraction(25,15)*i], color=t)
	plt.plot([40+Fraction(10,15)*i,50],[40+Fraction(10,15)*i,50-Fraction(50,15)*i], color=t)
	plt.plot([25+i,40+Fraction(10,15)*i],[100-4*i,40+Fraction(10,15)*i], color=t)
	plt.plot([25+Fraction(25,15)*i,50-Fraction(10,15)*i],[100-Fraction(50,15)*i,50-Fraction(10,15)*i], color=t)


xlim(-1, 51)
ylim(-1, 101)
plt.axis('off')
plt.savefig("parallel_expanse.png",dpi=300, bbox_inches='tight',pad_inches=0, facecolor="black")


