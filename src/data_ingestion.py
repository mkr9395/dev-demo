import pandas as pd 
import numpy as np 
import pathlib
import os

from pathlib import Path


df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

df = df.iloc[:,3:]

df = df[df['Length of Membership'] > 1]

joined_path = Path.joinpath(Path.cwd() / 'data')


df.drop(columns=['Avg. Session Length'],inplace=True)
df.to_csv(joined_path/'customer.csv',index=False)