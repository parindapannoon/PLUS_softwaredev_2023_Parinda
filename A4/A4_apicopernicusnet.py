# -*- coding: utf-8 -*-
"""A4_APICopernicusNet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ih2kcTw_Z3_qYniH7zm261ftLRQKeUfe

#**Step1: Access data via CDS API**
The Climate Data Store (CDS) FROM Copernicus Application Program Interface (API) is a service providing programmatic access to CDS data.The CDS API client is a python based library. It provides support for both Python 2.7.x and Python 3. https://cds.climate.copernicus.eu/api-how-to
"""

#You can Install the CDS API client via the package management system pip
!pip3 install cdsapi

"""####**Use the CDS API client for data access**
Install the CDS API key, If you don't have an account, please self register at the [CDS registration page](https://cds.climate.copernicus.eu/user/register?destination=%2F%23!%2Fhome) and go to the steps below.
"""

#please register at the CDS registration page so you get a key
url = 'url: https://cds.climate.copernicus.eu/api/v2'
key= 'insert your key'

"""This data set provides complete historical reconstruction of meteorological conditions favourable to the start, spread and sustainability of fires. The fire danger metrics provided are part of a vast dataset produced by the Copernicus Emergency Management Service for the European Forest Fire Information System (EFFIS). [Fire danger indices historical data](https://cds.climate.copernicus.eu/cdsapp#!/dataset/cems-fire-historical?tab=overview)
The api call must follow the syntax:
"""

#get API request from the dataset
import cdsapi

c = cdsapi.Client(url = 'https://cds.climate.copernicus.eu/api/v2',
key= 'insert your key')

c.retrieve(
    'cems-fire-historical',
    {
        'format': 'zip',
        'product_type': 'reanalysis',
        'variable': 'fire_weather_index',
        'version': '4.0',
        'dataset': 'Consolidated dataset',
        'year': [
            '2014','2016','2022',
        ],
        'month': '04',
        'day': [
            '10', '16', '20',
        ],
    },
    '/content/download.zip')

#extract the zipfile
import zipfile
with zipfile.ZipFile("/content/download.zip", 'r') as zip_ref:
    zip_ref.extractall("/content")

"""#**Step2: Working with Xarray**
This assignment I use Xarray for handling real world climate data in form of NetCDF format. Xarray is an Python Library for performing multidimensional data analysis, handling geospatial coordinates, time series and among other dimensions. NetCDF file format provides xarray with a natural and portable serialization format. NetCDF is very popular in the geosciences, and there are existing libraries for reading and writing netCDF in many programming languages, including Python. [Xarray Document](https://docs.xarray.dev/en/stable/getting-started-guide/why-xarray.html)
"""

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

"""##**Function1: open NetCDF dataset**
Open_dataset method is used to open NetCDF file which is Fire danger indices.
"""

def open_netcdf(netcdf):
    """
    open fire historical data from a downloaded NetCDF file.

    Args:
        netcdf path (str): A file path.

    Returns:
        Fire danger indices historical data in form of 3 dimensional xarray dataset; time, lat, lon.
    """
    netcdf = '/content/ECMWF_FWI_FWI_20140410_1200_hr_v4.0_con.nc'
    f = xr.open_dataset(netcdf)
    return f
netcdf = '/content/ECMWF_FWI_FWI_20140410_1200_hr_v4.0_con.nc'
f = xr.open_dataset(netcdf)
open_netcdf.__doc__

#print data array
f

# General info on the data
f.info

# Get the list of variables
f.data_vars

# Get the list of dimensions
f.coords

# Get info on one specific variable (here thetao)
f.fwi

# Get info on dimensions
f.time, f.latitude, f.longitude

"""##**Function2: Select data variable and timestep**
Select the point of time together with a fire data. In this data there is only 1 data variable which is "fwi" (Fire weather index)
"""

def select_data(variable, timestep):
    """
    Filter data variable and timestep in Xarray.

    Args:
        variable (str): represent the main data of interest in a dataset.
        timestep (str): represent time.

    Returns:
        The Fire data with timestep according to selected data.
    """
    subset = f[variable].sel(time = slice(timestep))
    return subset

#in this case I choose "fwi" data and "10 April 2014"
subset = f["fwi"].sel(time = slice("2014-04-10"))
subset
select_data.__doc__

## Plot
subset.plot(size = 8)

plt.show()

"""The map shows how Forest weather index distributes entire the world in 2014.

##**Function3: select time and longitude**
Select the point of time together along longitude. It allows you to select any longitude and also included nearest longitude for you if the longitude that you indicate does not have data.
"""

def plot_NetCDFdata(timeindex, lon):
    """
    Calls xarray plotting function based on the dimensions of the squeezed DataArray.

    Args:
        timeindex (int): represent given index in the timestep list.
        lon (int): represent longitude.

    Returns:
        The Fire danger index graph in each Latitude according to selected timestep and longitude.
    """
    return subset.isel(time=timeindex).sel(longitude=lon, method='nearest').plot()

#in this case I choose longitude -60
subset.isel(time=0).sel(longitude=-60, method='nearest').plot()
plot_NetCDFdata.__doc__

"""The graph shows how forest fire index changes according to the latitude. You can see that there is an high point around latitude 30. So this is a way how to visualize geospatial NetCDF data."""

#summarize mean value of this selected data
meanfire = subset.mean()
meanfire

#you can convert data to dataframe to see all the data as a table
df = f.to_dataframe()
df