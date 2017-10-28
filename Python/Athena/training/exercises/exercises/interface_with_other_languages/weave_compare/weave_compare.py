""" 
Weave Comparison
----------------

Compare the speed of NumPy, weave.blitz and weave.inline for the following
equation::
    
        result=a+b*(c-d)
    
Set up all arrays so that they are one-dimensional and have 1 million 
elements in them.

See: :ref:`weave-compare-solution`.
"""
import time

from numpy import arange, empty, float64
from scipy import weave

N = 1000000

a = arange(N,dtype=float64)
b = arange(N,dtype=float64)
c = arange(N,dtype=float64)
d = arange(N,dtype=float64)

result = empty(N,dtype=float64)

t1= time.clock()
result = a + b*(c-d)
t2=time.clock()
numpy_time = t2-t1

# Now do the weave.blitz and weave.inline versions.


    
    