FROM continuumio/miniconda3
RUN conda install -y -c pyviz pyviz
RUN conda install -y xarray holoviews geoviews cartopy hvplot pandas
WORKDIR /app
COPY alos_avnir2_ndwi.ipynb /app
COPY data/ /app/data/
