# %%
"""
<table class="ee-notebook-buttons" align="left">
    <td><a target="_blank"  href="https://github.com/giswqs/geemap/tree/master/examples/template/template.ipynb"><img width=32px src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a></td>
    <td><a target="_blank"  href="https://nbviewer.jupyter.org/github/giswqs/geemap/blob/master/examples/template/template.ipynb"><img width=26px src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" />Notebook Viewer</a></td>
    <td><a target="_blank"  href="https://colab.research.google.com/github/giswqs/geemap/blob/master/examples/template/template.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run in Google Colab</a></td>
</table>
"""

# %%
"""
## Install Earth Engine API and geemap
Install the [Earth Engine Python API](https://developers.google.com/earth-engine/python_install) and [geemap](https://geemap.org). The **geemap** Python package is built upon the [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) and [folium](https://github.com/python-visualization/folium) packages and implements several methods for interacting with Earth Engine data layers, such as `Map.addLayer()`, `Map.setCenter()`, and `Map.centerObject()`.
The following script checks if the geemap package has been installed. If not, it will install geemap, which automatically installs its [dependencies](https://github.com/giswqs/geemap#dependencies), including earthengine-api, folium, and ipyleaflet.
"""

# %%
# Installs geemap package
import subprocess

try:
    import geemap
except ImportError:
    print("Installing geemap ...")
    subprocess.check_call(["python", "-m", "pip", "install", "geemap"])

# %%
import ee
import geemap

# %%
"""
## Create an interactive map 
The default basemap is `Google Maps`. [Additional basemaps](https://github.com/giswqs/geemap/blob/master/geemap/basemaps.py) can be added using the `Map.add_basemap()` function. 
"""

# %%
Map = geemap.Map(center=[40, -100], zoom=4)
Map

# %%
"""
## Add Earth Engine Python script 
"""

# %%
# Add Earth Engine dataset
import math

# Extract MODIS QA information from the "state_1km" QA band
# and use it to mask out cloudy and deep ocean areas.
#
# QA Band information is available at:
# https:#lpdaac.usgs.gov/products/modis_products_table/mod09ga
# Table 1: 1-kilometer State QA Descriptions (16-bit)


#*
 # Returns an image containing just the specified QA bits.
 #
 # Args:
 #   image - The QA Image to get bits from.
 #   start - The first bit position, 0-based.
 #   end   - The last bit position, inclusive.
 #   name  - A name for the output image.
 #
def getQABits(image, start, end, newName):
    # Compute the bits we need to extract.
    pattern = 0
    for i in range(start, end, 1):
       pattern += math.pow(2, i)

    return image.select([0], [newName]) \
                  .bitwiseAnd(pattern) \
                  .rightShift(start)


# Reference a single MODIS MOD09GA image.
image = ee.Image('MODIS/006/MOD09GA/2012_10_11')

# Select the QA band
QA = image.select('state_1km')

# Get the cloud_state bits and find cloudy areas.
cloud = getQABits(QA, 0, 1, 'cloud_state') \
                    .expression("b(0) == 1 || b(0) == 2")

# Get the land_water_flag bits.
landWaterFlag = getQABits(QA, 3, 5, 'land_water_flag')

# Create a mask that filters out deep ocean and cloudy areas.
mask = landWaterFlag.neq(7).And(cloud.Not())

# Add a map layer with the deep ocean and clouds areas masked out.
Map.addLayer(image.updateMask(mask),
  {
    'bands': ['sur_refl_b01', 'sur_refl_b04', 'sur_refl_b03'],
    'min': -100,
    'max': 2000
  }, 'MOD09GA 143'
)

# Add a semi-transparent map layer that displays the clouds.
Map.addLayer(
    cloud.updateMask(cloud),
    {'palette': 'FFFFFF', 'opacity': 0.8},
    'clouds'
)


# %%
"""
## Display Earth Engine data layers 
"""

# %%
Map.addLayerControl()  # This line is not needed for ipyleaflet-based Map.
Map
