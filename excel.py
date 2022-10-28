#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 09:57:59 2022

@author: dennytsai
"""

import time
import datetime
import pandas as pd


tickers = ['IFNNY', 'CL=F', 'BZ=F']
interval = '1d' #1we, 1m available
period1 = int(time.mktime(datetime.datetime(2022, 1, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 7, 29, 23, 59).timetuple())) #mktime convert it to sec values.

xlwriter = pd.ExcelWriter('RECENT_prices.xlsx', engine='openpyxl')
for ticker in tickers:
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    df = pd.read_csv(query_string)
    df.to_excel(xlwriter, sheet_name=ticker, index=False)
    print(df)
  

xlwriter.save()