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
#*
 # @fileoverview Earth Engine Developer's Guide examples contained in
 #   the Global Surface Water tutorial, page 3.
 #

# [START 03_final_script]
###############################
# Asset List
###############################

gsw = ee.Image('JRC/GSW1_0/GlobalSurfaceWater')
occurrence = gsw.select('occurrence')
# [START change_intensity_object]
change = gsw.select("change_abs")
# [END change_intensity_object]
roi = ee.Geometry.Polygon(
        [[[-74.17213, -8.65569],
          [-74.17419, -8.39222],
          [-74.38362, -8.36980],
          [-74.43031, -8.61293]]])

###############################
# Constants
###############################

VIS_OCCURRENCE = {
    'min':0,
    'max':100,
    'palette': ['red', 'blue']
}
# [START vis_occurrence_change]
VIS_CHANGE = {
    'min':-50,
    'max':50,
    'palette': ['red', 'black', 'limegreen']
}
# [END vis_occurrence_change]
VIS_WATER_MASK = {
  'palette': ['white', 'black']
}

###############################
# Calculations
###############################

# Create a water mask layer, and set the image mask so that non-water areas are transparent.
water_mask = occurrence.gt(90).mask(1)

# [START histogram_chart]
# Generate a histogram object and print it to the console tab.
histogram = ui.Chart.image.histogram({
  'image': change,
  'region': roi,
  'scale': 30,
  'minBucketWidth': 10
})
histogram.setOptions({
  'title': 'Histogram of surface water change intensity.'
})
# [END histogram_chart]
print(histogram)

###############################
# Initialize Map Location
###############################

# Uncomment one of the following statements to center the map on
# a particular location.
# Map.setCenter(-90.162, 29.8597, 10);   # New Orleans, USA
# Map.setCenter(-114.9774, 31.9254, 10); # Mouth of the Colorado River, Mexico
# Map.setCenter(-111.1871, 37.0963, 11); # Lake Powell, USA
# Map.setCenter(149.412, -35.0789, 11);  # Lake George, Australia
# Map.setCenter(105.26, 11.2134, 9);     # Mekong River Basin, SouthEast Asia
# Map.setCenter(90.6743, 22.7382, 10);   # Meghna River, Bangladesh
# Map.setCenter(81.2714, 16.5079, 11);   # Godavari River Basin Irrigation Project, India
# Map.setCenter(14.7035, 52.0985, 12);   # River Oder, Germany & Poland
# Map.setCenter(-59.1696, -33.8111, 9);  # Buenos Aires, Argentina\
# [START addLayer_change_intensity]
Map.setCenter(-74.4557, -8.4289, 11);  # Ucayali River, Peru
# [END addLayer_change_intensity]

###############################
# Map Layers
###############################

Map.addLayer({
  'eeObject': water_mask,
  'visParams': VIS_WATER_MASK,
  'name': '90% occurrence water mask',
  'shown': False
})
Map.addLayer({
  'eeObject': occurrence.updateMask(occurrence.divide(100)),
  'name': "Water Occurrence (1984-2015)",
  'visParams': VIS_OCCURRENCE,
  'shown': False
})
# [START addLayer_change_intensity]
Map.addLayer({
  'eeObject': change,
  'visParams': VIS_CHANGE,
  'name': 'occurrence change intensity'
})
# [END addLayer_change_intensity]
# [END 03_final_script]

# [START histogram_reducer]
# Calculate a change intensity for the region of interest.
histogram = change.reduceRegion({
  'reducer': ee.Reducer.histogram(),
  'geometry': roi,
  'scale': 30,
  'bestEffort': True,
})
print(histogram)
# [END histogram_reducer]


# %%
"""
## Display Earth Engine data layers 
"""

# %%
Map.addLayerControl()  # This line is not needed for ipyleaflet-based Map.
Map
