"""
  Name     : 4375OS_07_13_number_sotkcs_vs_porttfolio_volatility.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

from matplotlib.pyplot import *
n=[1,2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,75,100,200,300,400,500,600,700,800,900,1000]
port_sigma=[0.49236,0.37358,0.29687,0.26643,0.24983,0.23932,0.23204,0.22670,
0.22261,0.21939,0.21677,0.21196,0.20870,0.20634,0.20456,0.20316,0.20203,0.19860,
0.19686,0.19432,0.19336,0.19292,0.19265,0.19347,0.19233,0.19224,0.19217,0.19211,0.19158]
xlim(0,50)
ylim(0.1,0.4)
hlines(0.19217, 0, 50,  colors='r', linestyles='dashed')
annotate('', xy=(5, 0.19), xycoords = 'data',xytext = (5, 0.28), textcoords = 'data',
    arrowprops = {'arrowstyle':'<->'})
annotate('', xy=(30, 0.19), xycoords = 'data',xytext = (30, 0.1), textcoords = 'data',
    arrowprops = {'arrowstyle':'<->'})
annotate('Total portfolio risk', xy=(5,0.3),xytext=(25,0.35),arrowprops=dict(facecolor='black',shrink=0.02))         
figtext(0.15,0.4,"Diversiable risk")
figtext(0.65,0.25,"Nondiversifiable risk")
plot(n[0:17],port_sigma[0:17])
title("Relationship between n and portfolio risk")
xlabel("Number of stocks in a portfolio")
ylabel("Ratio of Portfolio std to std of one stock")
show()

