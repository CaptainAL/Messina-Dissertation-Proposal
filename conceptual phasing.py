# -*- coding: utf-8 -*-
"""
Created on Tue Jul 01 15:46:56 2014

@author: Alex
"""
import pandas as pd
import datetime

fig, (ax) = plt.subplots(1,1)
plt.xkcd()


start = datetime.datetime(2014,1,1)
end = datetime.datetime(2014,12,31)
dates= pd.date_range(start,end,freq='M')
swell = sin(np.linspace(0.1,3,12))+1
sediment = [2,1.5,2,1.5,1,1.75,1.70,1.8,1.25,1.8,2.1,1.9]

df = pd.DataFrame.from_dict({'swell height':swell,'sediment loading':sediment,'months':dates}).set_index('months')


ax.plot_date(df.index,df['sediment loading'],'r-')
ax2 = fig.add_axes(ax.get_position(), frameon=False, sharex=ax,sharey=ax)
ax2.plot_date(df.index,df['swell height'],'b-')

ax.set_ylim(.5,2.5)
ax.set_ylabel('Sediment (tons/month)')
ax2.yaxis.set_ticks_position('right'),ax2.yaxis.set_label_position('right')
ax2.set_ylabel('Mean monthly swell height (m)')
plt.suptitle('Hypothetical phasing of monthly sediment loading and swell height')