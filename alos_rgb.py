
# coding: utf-8

# In[ ]:


import numpy as np
import numba
import xarray as xr
import hvplot.xarray
import geoviews as gv
import holoviews as hv
import cartopy.crs as ccrs
gv.extension('bokeh', logo=False)
hv.extension('bokeh', logo=False)
renderer = hv.Store.renderers['bokeh'].instance(mode='server', holomap='server')


# In[ ]:


ds = xr.open_dataset('alos_rgb.nc')


# In[ ]:


outcrs = ccrs.epsg(6676)

s = ds.hvplot.rgb('x','y',z='rgb', bands='bands',crs=outcrs, width=700, height=500, rasterize=True)

url = 'https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{Z}/{X}/{Y}.jpg'
geomap = gv.WMTS(url, crs=outcrs)

ds.close()
fig = s * geomap

doc,_ = renderer(fig)
doc.title = "Oigawa_Visualized_by_Alos-Avnir2"

