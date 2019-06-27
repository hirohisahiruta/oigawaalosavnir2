FROM continuumio/miniconda3
RUN conda install -y bokeh xarray holoviews geoviews cartopy numpy pandas
WORKDIR /app
COPY alos_avnir2_ndwi.py /app
COPY data /app/data