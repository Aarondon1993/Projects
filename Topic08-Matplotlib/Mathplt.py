# Aaron Donnelly
# This program will graph the function f(x)=x, g(x)=x2 and h(x)=x3 in the range [0,4]
# IPython log file

import numpy as np
x = np.arange(0,4)
g= x**2
h= x**3
import matplotlib.pyplot as plt
plt.plot(x,"y",g,"g",h,"r",label= "Topic08-Mathplotlib")
plt.savefig("Matplotlib task week 8")

