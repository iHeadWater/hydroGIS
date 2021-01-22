# -*- coding: utf-8 -*-
# please read UserMannual.docx

import ee
ee.Initialize()
from osgeo import ogr

# date for NLDAS
dataset = ee.ImageCollection('NASA/NLDAS/FORA0125_H002').filter(ee.Filter.date('2000-01-01', '2001-1-5'))
# don't change!
img = dataset.select(['temperature',"total_precipitation","pressure","wind_u","wind_v","longwave_radiation","convective_fraction","potential_energy","potential_evaporation","shortwave_radiation"])

#ds = ogr.Open('shape/Demo_Shape/demo_shape.shp',0) # demo shape
# read shape(3 basins)
ds = ogr.Open('shape/basins.shp',0)
lyr = ds.GetLayer(0) # get the first layer and it has only one layer
num_basin = lyr.GetFeatureCount() # get number of basins

for i_num in range(num_basin):    
    
    i_lyr_geom = i_lyr.geometry() # geometry information in the shape 
    i_lyr_json = i_lyr_geom.ExportToJson() # convert to GeoJSON. Sometimes, points are too much！
    i_ConvexHull = i_lyr_geom.ConvexHull().ExportToIsoWkt() # you can use the convex hull to get the result more quickly.
    
    # use the convex hull as roi
    a=i_ConvexHull[10:-2]
    b=a.split(',')
#    c = [[i.replace(" ",",")] for i in b]
    d = [map(eval,i.split(' ')) for i in b]
    i_roi = ee.Geometry.Polygon([d])

# # i_lyr_bou = i_lyr_geom.GetEnvelope()
# # use all points as roi, but sometimes it too slow to get result and you can get timeout
#    i_lyr_ee = ee.Geometry.Polygon(eval(i_lyr_json[36:-2]))
#    i_roi = i_lyr_ee
    
    # don't change position!   
    def get_Mean(image):
        dict = image.reduceRegion(
            reducer = ee.Reducer.mean(),
            geometry = i_roi);
        image = image.set('Meann',dict)
        return image    
    
    # your result name
    i_name_basin = 'basin'+str(i_num)+'_s'
    print i_name_basin
    # get result for every basin average
    result_mean = img.map(get_Mean)
    # set task for export
    task = ee.batch.Export.table.toDrive(
            collection = result_mean, 
            description = 'PSU_task_'+str(i_num), 
            folder = 'PSU_GEE', 
            fileNamePrefix =i_name_basin, 
            fileFormat  = 'CSV',
            selectors = ["system:index", "Meann"]);
    # start the task
    task.start()

    
