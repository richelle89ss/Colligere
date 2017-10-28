"""
  Name     : 4375OS_12_07_save_call_put_pickle_format.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""


from pandas.io.data import Options
import datetime
import pandas as pd

def call_data(tickrr,exp_date):
    x = Options(ticker,'yahoo')
    data= x.get_call_data(expiry=exp_date)
    return data
ticker='IBM'
exp_date=datetime.date(2014,2,28)
c=call_data(ticker,exp_date)
print c.head()
callsFeb2014=pd.DataFrame(c,columns=['Strike','Symbol','Chg','Bid','Ask','Vol','Open Int'])
callsFeb2014.to_pickle('c:/temp/callsFeb2014.pickle')


def put_data(tickrr,exp_date):
    x = Options(ticker,'yahoo')
    data= x.get_put_data(expiry=exp_date)
    return data
p=put_data(ticker,exp_date)
putsFeb2014=pd.DataFrame(p,columns=['Strike','Symbol','Chg','Bid','Ask','Vol','Open Int'])
putsFeb2014.to_pickle('c:/temp/putsFeb2014.pickle')

