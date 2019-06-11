FROM continuumio/miniconda3
RUN conda install -y bokeh xarray holoviews geoviews hvplot cartopy
# FROM python:3.6
WORKDIR /app
COPY alos_rgb.py /app
COPY alos_rgb.nc /app