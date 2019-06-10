
# coding: utf-8

# In[ ]:


import xarray as xr
import hvplot.xarray
import geoviews as gv
import cartopy.crs as ccrs
import holoviews as hv
# import holoviews.plotting.bokeh
# hv.extension('bokeh', logo=False)
renderer = hv.Store.renderers['bokeh'].instance(mode='server', holomap='server')


# In[ ]:


air_ds = xr.tutorial.open_dataset('air_temperature').load()

s = air_ds.hvplot.quadmesh(
    'lon', 'lat', 'air', projection=ccrs.Orthographic(-90, 30),
    global_extent=True, width=600, height=540, cmap='viridis'
) * gv.feature.coastline


# In[ ]:


doc,_ = renderer(s)

