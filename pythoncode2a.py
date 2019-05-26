#!/usr/bin/env python3
import pandas as pd
import numpy as np

df=pd.read_csv('/home/edith/A1/flightdelays1.csv')

df=df.loc[df['Origin']=='SFO',:]

df[['ArrDelay','Origin']].head(3).to_csv('SFO.csv')

print(open('SFO.csv').read())