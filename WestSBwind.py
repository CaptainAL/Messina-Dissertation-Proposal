# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 04:47:07 2014

@author: Alex
"""

import pandas as pd
import datetime as dt

datadir = 'C:/Users/Alex/Desktop/'
datafile = datadir+'WestSBwind.xlsx'

def my_parser(x):
        try:
            date_time = str(x).split(' ')
            year = date_time[0].split('/')[2]
            month = date_time[0].split('/')[0]
            day= date_time[0].split('/')[1]
            hour=date_time[1].split(':')[0]
            minute=date_time[1].split(':')[1]
            parsed=dt.datetime(int(year),int(month),int(day),int(hour),int(minute))
        except:
            parsed = pd.to_datetime(np.nan)
        return parsed

XL = pd.ExcelFile(datafile)

wind = XL.parse('Sheet1',header=0,skiprows=0,na_values=['9999','999'])
wind = wind[1:].astype('str')
wind['datetimes'] = wind['MM']+'/'+wind['DD']+'/'+wind['#YY']+' '+wind['hh']+':'+wind['mm']

wind['datetimes'] = wind['datetimes'].apply(my_parser)
wind = wind.set_index('datetimes')

wind['WSPD']=wind['WSPD'].astype('float')
wind['speed kt']=wind['WSPD']*1.9438444924


