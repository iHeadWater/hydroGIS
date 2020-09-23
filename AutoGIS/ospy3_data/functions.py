# function to copy fields (not the data) from one layer to another
# parameters:
#   fromLayer: layer object that contains the fields to copy
#   toLayer: layer object to copy the fields into
def copyFields(fromLayer, toLayer):
  featureDefn = fromLayer.GetLayerDefn()
  for i in range(featureDefn.GetFieldCount()):
    toLayer.CreateField(featureDefn.GetFieldDefn(i))

# function to copy attributes from one feature to another
# (this assumes the features have the same attribute fields!)
# parameters:
#   fromFeature: feature object that contains the data to copy
#   toFeature: feature object that the data is to be copied into
def copyAttributes(fromFeature, toFeature):
  for i in range(fromFeature.GetFieldCount()):
    fieldName = fromFeature.GetFieldDefnRef(i).GetName()
    toFeature.SetField(fieldName, fromFeature.GetField(fieldName))