"""
  Name     : 4375OS_11_37_simulation_efficient_frontier2stocks.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 2/9/2014
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import numpy as np
import scipy as sp
import pandas as pd
from datetime import datetime as dt
from scipy.optimize import minimize
# Step 1: input area
mean_0=(0.15,0.25) # mean returns for 2 stocks
std_0= (0.10,0.20) # standard deviations for 2 stocks
corr_=0.2          # correlation between 2 stocks
n=1000             # number of simuations (returns) for each stock
# Step 2: Generate two uncorrelated time series 
n_stock=len(mean_0)
sp.random.seed(12345) # could generate the same random numbers 
x1=sp.random.normal(loc=mean_0[0],scale=std_0[0],size=n)
x2=sp.random.normal(loc=mean_0[1],scale=std_0[1],size=n)
if(any(x1)<=-1.0 or any(x2)<=-1.0):
    print ('Error: return is <=-100%')
# Step 3: Generate two correlated time series 
index_=pd.date_range(start=dt(2001,1,1),periods=n,freq='d')
y1=pd.DataFrame(x1,index=index_)
y2=pd.DataFrame(corr_*x1+sqrt(1-corr_**2)*x2,index=index_)
# step 4: generate a return matrix called R
R0=pd.merge(y1,y2,left_index=True,right_index=True)
R=np.array(R0)
# Step 5: define a few functions
def objFunction(W, R, target_ret): 
    stock_mean=np.mean(R,axis=0)  
    port_mean=np.dot(W,stock_mean)           # portfolio mean
    cov=np.cov(R.T)                          # var-covar matrix
    port_var=np.dot(np.dot(W,cov),W.T)       # portfolio variance
    penalty = 2000*abs(port_mean-target_ret) # penalty 4 deviation 
    return np.sqrt(port_var) + penalty       # objective function 
# Step 6: estimate optimal portfolo for a given return 
out_mean,out_std,out_weight=[],[],[] 
stockMean=np.mean(R,axis=0)    
for r in np.linspace(np.min(stockMean), np.max(stockMean), num=100):
    W = ones([n_stock])/n_stock                      # starting:equal w 
    b_ = [(0,1) for i in range(n_stock)]             # bounds
    c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. })# constraint
    result=minimize(objFunction,W,(R,r),method='SLSQP',constraints=c_, bounds=b_)    
    if not result.success:                    # handle error
        raise BaseException(result.message) 
    out_mean.append(round(r,4))               # a few decimal places
    std_=round(np.std(np.sum(R*result.x,axis=1)),6)
    out_std.append(std_)
    out_weight.append(result.x) 
# Step 7: plot the efficient frontier
title('Simulation for an Efficient Frontier from given 2 stocks')
xlabel('Standard Deviation of the 2-stock Porfolio (Risk)')
ylabel('Return of the2-stock portfolio')
figtext(0.2,0.80,' mean = '+str(stockMean))
figtext(0.2,0.75,' std  ='+str(std_0))
figtext(0.2,0.70,' correlation ='+str(corr_))
plot(np.array(std_0),np.array(stockMean),'o',markersize=8)
plot(out_std,out_mean,'--',linewidth=3)