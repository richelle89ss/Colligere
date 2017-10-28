""" 
Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a for loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

Implement integration of the same function using Riemann sums or the
trapezoidal rule.

"""
from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, subplot, legend, title

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)

# calculate the derivative dy/dx numerically.
# First, calculate the distance between adjacent pairs of
# x and y values.
dy = y[1:]-y[:-1]
dx = x[1:]-x[:-1]

# Now divide to get "rise" over "run" for each interval.
dy_dx = dy/dx

# Assuming central differences, these derivative values
# centered in-between our original sample points.
centers_x = (x[1:]+x[:-1])/2.0

# Plot our derivative calculation.  It should match up
# with the cos function since the derivative of sin is
# cos.    
subplot(1,2,1)
plot(centers_x, dy_dx,'rx', centers_x, cos(centers_x),'b-')
title(r"$\rm{Derivative\ of}\ sin(x)$")

# Trapezoidal rule integration.
avg_height = (y[1:]+y[:-1])/2.0
int_sin = cumsum(dx * avg_height)

# Plot our integration against -cos(x) - -cos(0)  
closed_form = -cos(x)+cos(0)
subplot(1,2,2)
plot(x[1:], int_sin,'rx', x, closed_form,'b-')
legend(('numerical', 'actual'))
title(r"$\int \, \sin(x) \, dx$")
show()

