# FROM python:3.6
# WORKDIR /app
# RUN pip install bottle
# COPY app.py /app
# CMD ["python3", "app.py"]

FROM continuumio/miniconda3
# MAINTAINER Antonia Elek <antoniaelek at hotmail.com>
RUN conda install -y bokeh xarray holoviews geoviews hvplot cartopy
# WORKDIR /vol

#VOLUME '/vol'
#EXPOSE 5006
#ENTRYPOINT ["bokeh","serve","--show","vol/hvplottest.py","--allow-websocket-origin=*"]
# ENTRYPOINT ["bokeh","serve","/vol/hvplottest.py","--port","3128","--allow-websocket-origin=52.199.105.98:80"]