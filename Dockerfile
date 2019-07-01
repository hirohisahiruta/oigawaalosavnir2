FROM continuumio/miniconda3
# RUN conda update -n base conda \
  # && conda create -n py36 python=3.6 anaconda \
  # && . activate py36 \
  # && 
# RUN conda install -y bokeh xarray holoviews geoviews cartopy numpy pandas
RUN conda install -y xarray holoviews geoviews cartopy hvplot pandas
WORKDIR /app
# COPY alos_avnir2_ndwi.ipynb /app
COPY data/ /app/data/
COPY tmp.py /app