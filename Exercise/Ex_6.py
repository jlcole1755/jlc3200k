#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise06"
#if arcpy.Exists("cities.shp"):
#    arcpy.CopyFeatures_management("cities.shp", "results/cities_copy.shp")


#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise06"
#fclist = arcpy.ListFeatureClasses()
#for fc in fclist:
#    fcdescribe = arcpy.Describe(fc)
#    print "Name: " + fcdescribe.name
#    print "Data type: " + fcdescribe.dataType

#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise06"
#fclist = arcpy.ListFeatureClasses()
#for fc in fclist:
#    arcpy.CopyFeatures_management (fc,"G:/Exercise for Python/Python/Data/Exercise06/Results/" + fc) 


#import arcpy
#from arcpy import env
#env.overwrightOutput = True-------  #This line of code makes it possible for the script to overwrite existing files. 
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise06"
#arcpy.CreateFileGDB_management("G:/Exercise for Python/Python/Data/Exercise06/Results", "NM.gdb")
#fclist = arcpy.ListFeatureClasses()
#for fc in fclist:
#    fcdesc = arcpy.Describe(fc)
#    arcpy.CopyFeatures_management(fc,"G:/Exercise for Python/Python/Data/Exercise06/Results/NM.gdb/" + fcdesc.basename)


#import arcpy
#from arcpy import env
#env.overwrightOutput = True --------  #This line of code makes it possible for the script to overwrite existing files.
#env.workspace = 
#fieldlist = arcpy.ListFields("cities.shp")
#for field in fieldlist:
#    print field.name + "" + field.type


##########EXERCISES
import arcpy
from arcpy import env
env.workspace = "G:/Exercise for Python/Python/Data/Exercise06"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    desc = arcpy.Describe(fc)
    print "{0} is a {1} feature class".format(desc.basename, desc.shapeType)
import arcpy
from arcpy import env
env.workspace = "G:/Exercise for Python/Python/Data/Exercise06"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    desc = arcpy.Describe(fc)
    if desc.shapeType == "polygon":
        arcpy.Copy_management (fc, "G:/Exercise for Python/Python/Data/Exercise06" + fc)

