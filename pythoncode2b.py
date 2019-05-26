#!/usr/bin/env python3

import pandas as pd
import numpy as np

df=pd.read_csv('/home/edith/A1/flightdelays1.csv',usecols=['Dest','FlightNum'])

dest_counts= df['Dest'].value_counts()

print(dest_counts.head(3))
