
# coding: utf-8

# In[ ]:


import xarray as xr
import geoviews as gv
import holoviews as hv
import cartopy.crs as ccrs
# import numpy as np
import pandas as pd
# from holoviews.operation.datashader import rasterize

gv.extension('bokeh', logo=False)
hv.extension('bokeh', logo=False)
renderer = hv.Store.renderers['bokeh'].instance(mode='server', holomap='server')


# In[ ]:


# ds = xr.open_dataset('data/ndwi.nc')


# In[ ]:


# outcrs = ccrs.epsg(6676)

# figs = {}
# for i, t in enumerate(ds.t.values):
#     dss = ds.isel(t=i)
#     ndwi = dss['ndwi']
#     ndwi = np.where(ndwi==0, np.nan, ndwi)
#     figs[t] = gv.Image((dss['x'], dss['y'], ndwi), crs=outcrs).options(cmap='gray_r',colorbar=True)

# hmap = gv.HoloMap(figs, kdims='time')

# url = 'https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{Z}/{X}/{Y}.jpg'
# geomap = gv.WMTS(url, crs=outcrs).options(width=500,height=400)


# In[ ]:


def parser(date):
    b = date.split(' ')
    c = b[1].split(':')
    return pd.datetime.strptime(b[0],'%Y/%m/%d') + pd.Timedelta(hours=int(c[0]), minutes=int(c[1])) 

f = r'data/kanza_Q.csv'
dfQ = pd.read_csv(f, engine='python', index_col=0, parse_dates=True, header=None, date_parser=parser)
dfQ = dfQ.replace(-9999, np.nan)

Q = hv.Curve( (dfQ.index,dfQ.values.flatten()),vdims='Discharge at Kanza' ).options(width=500,height=300)
# figs2 = {}
# for t in ds.t.values:
#     figs2[t] = hv.VLine(t).options(color='r',)
#     
# vl = gv.HoloMap(figs2, kdims='time')


# In[ ]:


# fig = ( geomap * rasterize(hmap, precompute=True) + Q * rasterize(vl, precompute=True) ).cols(1)
fig =  Q #* rasterize(vl, precompute=True) 

doc,_ = renderer(fig)
doc.title = "Oigawa_Visualized_by_Alos-Avnir2"

