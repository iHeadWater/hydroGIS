import _gdal

def GetBlockSize(band):
  x = _gdal.ptrcreate('int', 0, 2)
  _gdal.GDALGetBlockSize(band._o, x, _gdal.ptradd(x, 1))
  result = (_gdal.ptrvalue(x, 0), _gdal.ptrvalue(x, 1))
  _gdal.ptrfree(x)
  return result
