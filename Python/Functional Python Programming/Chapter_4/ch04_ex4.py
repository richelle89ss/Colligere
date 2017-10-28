#!/usr/bin/env python3
"""Functional Python Programming

Chapter 4, Example Set 4

Definitions of mean, stddev, Pearson correlation
and linear estimation.

http://en.wikipedia.org/wiki/Mean

http://en.wikipedia.org/wiki/Standard_deviation

http://en.wikipedia.org/wiki/Standard_score

http://en.wikipedia.org/wiki/Normalization_(statistics)

http://en.wikipedia.org/wiki/Simple_linear_regression
"""
import math

def s0( samples ):
    return sum(1 for x in samples) # sum(x**0 for x in samples)

def s1( samples ):
    return sum(samples) # sum(x**1 for x in samples)

def s2( samples ):
    return sum( x**2 for x in samples )

def mean( samples ):
    """Arithmetic mean.

    >>> d = [4, 36, 45, 50, 75]
    >>> mean(d)
    42.0
    """
    # return sum(samples)/len(samples)
    return s1(samples)/s0(samples)

def stdev( samples ):
    """Standard deviation.

    >>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
    >>> mean(d)
    5.0
    >>> stdev(d)
    2.0
    """
    N= len(samples) # s0(samples)
    return math.sqrt((s2(samples)/N)-(s1(samples)/N)**2)

def z( x, μ_x, σ_x ):
    """
    Compute a normalized score.

    >>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
    >>> list( z( x, mean(d), stdev(d) ) for x in d )
    [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]

    The above example recomputed mean and standard deviation.
    Not a best practice.
    """
    return (x-μ_x)/σ_x

def corr( sample1, sample2 ):
    """Pearson product-moment correlation.

    >>> xi= [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65,
    ...     1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83,] #  Height (m)
    >>> yi= [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29,
    ...     63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46,] #  Mass (kg)
    >>> round( corr( xi, yi ), 5 )
    0.99458
    """
    μ_1, σ_1 = mean(sample1), stdev(sample1)
    μ_2, σ_2 = mean(sample2), stdev(sample2)
    z_1 = (z( x, μ_1, σ_1 ) for x in sample1)
    z_2 = (z( x, μ_2, σ_2 ) for x in sample2)
    r = sum( zx1*zx2 for zx1, zx2 in zip(z_1, z_2) )/len(sample1)
    return r

def linest( x_list, y_list ):
    """Linear Least-Squares Estimation.

    >>> xi= [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65,
    ...     1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83,] #  Height (m)
    >>> yi= [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29,
    ...     63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46,] #  Mass (kg)
    >>> assert len(xi) == len(yi)
    >>> alpha, beta = linest(xi, yi)
    >>> round(alpha,3)
    -39.062
    >>> round(beta,3)
    61.272
    """
    r_xy= corr( x_list, y_list )
    μ_x, σ_x= mean(x_list), stdev(x_list)
    μ_y, σ_y= mean(y_list), stdev(y_list)
    beta= r_xy * σ_y/σ_x
    alpha= μ_y - beta*μ_x
    return alpha, beta

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
