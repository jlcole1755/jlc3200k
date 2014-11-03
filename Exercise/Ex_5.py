import arcpy
from arcpy import env
env.workspace = "G:/Exercise for Python/Python/Data/Exercise05"
arcpy.AddXY_management("hospitals.shp")

### import arcpy
### from arcpy import env
### env.workspace = "G:/Exercise for Python/Python/Data/Exercise05"
### arcpy.Dissolve_management("parks.shp", "parks_dissolved.shp", "PARK_TYPE", "", "FALSE")

import arcpy
default = "no extensions are available"
if arcpy.CheckExtension("3D") == "Available":
    ext_3D = "3D Analyst"
else:
    ext_3D = ""
if arcpy.CheckExtension("Network") == "Available":
    ext_network = "Network Analyst"
else:
    ext_network = ""
if arcpy.CheckExtension("Spatial") == "Available":
    ext_spatial = "Spatial Analyst"
else:
    ext_spatial = ""
print "The following extensions are available: " + ext_3D + ext_network + ext_spatial + default
