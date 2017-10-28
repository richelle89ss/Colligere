"""
  Name     : 4375OS_08_03_OLS.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import numpy as np
import statsmodels.api as sm
y=[1,2,3,4,2,3,4]
x=range(1,8)
x=sm.add_constant(x)
results=sm.OLS(y,x).fit()
print results.params
