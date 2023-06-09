## Objective
This Folium Heatmap notebook aims to process a dataset of crime incidents in the city of Chicago 2021, and use this data to create an animated heatmap displaying crime hotspots through time.
The Heatmaps use color to display a quantity that changes over two dimensions, also use color to display the magnitude of some quantity that varies in two dimensions.
In this case, I will show the density of crime reports on a map by creating heatmaps using Python.

Moreover, this task will be associated to our final project since we would like to utilize Folium to generate a disaster web map. Therefore, using Folium Heatmap will be useful for visualizing residential density so we can analyze damage probability in the study area.

## Results
There are 2 maps, the first one is density crime map, the second one shows actual crime location.
<img src="https://github.com/parindapannoon/PLUS_softwaredev_2023_Parinda/blob/c58339030278d12b0f222f40f55e5d1ad4db7e15/A3/giffile_heatmap.gif">
<img src= "https://github.com/parindapannoon/PLUS_softwaredev_2023_Parinda/blob/21fbc7d6658ffd65db80ecff155bef22f27b4c8b/A3/giffile2_heatmap.gif">
## Packages
This geo-python notebook consists of the following packages;
1. Folium: folium makes it easy to visualize data that’s been manipulated in Python on an interactive leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing rich vector/raster/HTML visualizations as markers on the map.  The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. folium supports both Image, Video, GeoJSON and TopoJSON overlays. https://python-visualization.github.io/folium/
2. Geopandas: GeoPandas is an open source project to make working with geospatial data in python easier. GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types. Geometric operations are performed by shapely. Geopandas further depends on fiona for file access and matplotlib for plotting. https://geopandas.org/en/stable/

See more libraries that I used in the notebook. Also, you can download the Html file in the folder to see the heatmap.

## Data
Data in this task are 1. Chicago boundary shapefile, 2. Chicago crime records 2021. The data can be downloaded from this link https://drive.google.com/drive/folders/1fjPaOxqGwUUHm98C0-Fzmk-fan4KBU9u?usp=sharing


This task is a part of the course Software developement 2023, University of Salzburg.
