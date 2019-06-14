FROM continuumio/miniconda3
RUN conda install -y bokeh xarray holoviews geoviews cartopy numpy pandas pytz
# FROM python:3.6
WORKDIR /app
COPY alos_rgb.py /app
COPY data/ /app/data/