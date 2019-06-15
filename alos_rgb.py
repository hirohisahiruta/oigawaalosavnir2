
# coding: utf-8

# # import module

# In[ ]:


import xarray as xr
import geoviews as gv
import holoviews as hv
import cartopy.crs as ccrs
import glob
import numpy as np
import pandas as pd
from pytz import timezone
from holoviews.operation.datashader import rasterize

gv.extension('bokeh', logo=False)
hv.extension('bokeh', logo=False)
renderer = hv.Store.renderers['bokeh'].instance(mode='server', holomap='server')


# In[ ]:


def parser(date):
    b = date.split(' ')
    c = b[1].split(':')
    return pd.datetime.strptime(b[0],'%Y/%m/%d') + pd.Timedelta(hours=int(c[0]), minutes=int(c[1])) 

f = r'data/kanza_Q.csv'
dfQ = pd.read_csv(f, engine='python', index_col=0, parse_dates=True, header=None, date_parser=parser)
dfQ = dfQ.replace(-9999, np.nan)

Q = hv.Curve( (dfQ.index,dfQ.values.flatten()),vdims='Discharge at Kanza' ).options(width=500,height=300)


# In[ ]:


fig = Q 

doc,_ = renderer(fig)
doc.title = "Oigawa_Visualized_by_Alos-Avnir2"

