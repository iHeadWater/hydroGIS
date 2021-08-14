import ogr, os, sys

def __getGeomName(geomType):
  ignore = ['wkbXDR', 'wkbNDR']
  if geomType is None:
    return None
  for const in vars(ogr):
    if const.startswith('wkb') and vars(ogr)[const] == geomType and not const in ignore:
      return const
  return None

def __isSpatial(layer):
  return layer.GetFeature(0).GetGeometryRef() is not None

def __countRows(layer):
  layer.ResetReading()
  n = 0
  row = layer.GetNextFeature()
  while row:
    n += 1
    row = layer.GetNextFeature()
  layer.ResetReading()
  return n

def printAtts(layer):
  if (not isinstance(layer, ogr.Layer)):
    print 'Parameter must be on OGR Layer object'
    sys.exit(1)
  featureDefn = layer.GetLayerDefn()
  if __isSpatial(layer):
    print 'The layer has %i features of type %s.' % (layer.GetFeatureCount(), __getGeomName(featureDefn.GetGeomType()))
  else:
    print 'The layer has %i non-spatial rows.' % (__countRows(layer))
  formatStr = ''
  for i in range(featureDefn.GetFieldCount()):
    formatStr = formatStr + '%(' + featureDefn.GetFieldDefn(i).GetName() + ')' + str(featureDefn.GetFieldDefn(i).GetWidth()) + 's     '
  vals = {}
  for i in range(featureDefn.GetFieldCount()):
    vals[featureDefn.GetFieldDefn(i).GetName()] = featureDefn.GetFieldDefn(i).GetName()
  print formatStr % vals
  row = layer.GetNextFeature()
  while row:
    for i in range(featureDefn.GetFieldCount()):
      vals[featureDefn.GetFieldDefn(i).GetName()] = row.GetFieldAsString(i)
    print formatStr % vals
    row = layer.GetNextFeature()

