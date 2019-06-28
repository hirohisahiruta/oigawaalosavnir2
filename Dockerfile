FROM continuumio/miniconda3
RUN conda update -n base conda \
  && conda create -n py36 python=3.6 anaconda \
  && . activate py36 \
  && conda install -y bokeh xarray holoviews geoviews cartopy numpy pandas
WORKDIR /app
COPY alos_avnir2_ndwi.ipynb /app
COPY data/ /app/data/