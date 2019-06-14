
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


# # make a xarray

# In[ ]:


time = []
for f in glob.glob('data/*.txt') : 

    with open(f) as fall : d = fall.readlines()
    timetxt = d[0][192:192+24]
    ts = pd.to_datetime(timetxt.strip(), format='%Y%m%d%H%M%S%f') 
    utc = timezone('UTC').localize(ts)
    jst = utc.astimezone(timezone('Asia/Tokyo'))
    time.append(jst.tz_localize(None))


fB1 = glob.glob('data/IMG-01*.tif')
fB2 = glob.glob('data/IMG-02*.tif')
fB3 = glob.glob('data/IMG-03*.tif')

l = []
for ffB1,ffB2,ffB3 in zip(fB1,fB2,fB3) :
    B1 = xr.open_rasterio(ffB1).values[0]
    B2 = xr.open_rasterio(ffB2).values[0]
    B3 = xr.open_rasterio(ffB3).values[0]
    alpha = np.where(B1<1, 0, 255)
    
    band = np.c_[
         B3[:,:,np.newaxis]
        ,B2[:,:,np.newaxis]
        ,B1[:,:,np.newaxis]
        ,alpha[:,:,np.newaxis]
            ]
    
    l.append(band)
    
bands = np.r_[l]
da = xr.open_rasterio(glob.glob('data/IMG-01*.tif')[0])

ds = xr.Dataset({ 'rgb': (['t','y','x','bands'], bands)}
                   , coords={'x': da['x'].values, 'y': da['y'].values, 't': time, 'bands':np.array([0,1,2,3])})

ds = ds.chunk({'t':1,'bands':1})


# In[ ]:


outcrs = ccrs.epsg(6676)

figs = {}
for i, t in enumerate(ds.t.values):
    dss = ds.isel(t=i)
    bands = dss['rgb'].data.compute()
    figs[t] = gv.RGB((dss['x'], dss['y'],  bands[:,:,0],  bands[:,:,1],  bands[:,:,2],  bands[:,:,3] ), vdims=list('RGBA') ,crs=outcrs)

hmap = gv.HoloMap(figs, kdims='time')

url = 'https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{Z}/{X}/{Y}.jpg'
geomap = gv.WMTS(url, crs=outcrs).options(width=500,height=400)


# In[ ]:


def parser(date):
    b = date.split(' ')
    c = b[1].split(':')
    return pd.datetime.strptime(b[0],'%Y/%m/%d') + pd.Timedelta(hours=int(c[0]), minutes=int(c[1])) 

f = r'data/kanza_Q.csv'
dfQ = pd.read_csv(f, engine='python', index_col=0, parse_dates=True, header=None, date_parser=parser)
dfQ = dfQ.replace(-9999, np.nan)

Q = hv.Curve( (dfQ.index,dfQ.values.flatten()),vdims='Discharge at Kanza' ).options(width=500,height=300)
figs2 = {}
for t in ds.t.values:
    figs2[t] = hv.VLine(t).options(color='r',)
    
vl = gv.HoloMap(figs2, kdims='time')


# In[ ]:


fig = ( geomap * rasterize(hmap, precompute=True) + Q * rasterize(vl, precompute=True) ).cols(1)

doc,_ = renderer(fig)
doc.title = "Oigawa_Visualized_by_Alos-Avnir2"

