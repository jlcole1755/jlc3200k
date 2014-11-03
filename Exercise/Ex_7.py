#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#fc = "airports.shp"
#cursor = arcpy.da.SearchCursor(fc, ["NAME"])
#for row in cursor:
#    print "Airport name ={0}".format(row[0])



#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#fc = "airports.shp"
#cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" = \'Seaplane Base\'')
#for row in cursor:
#    print row[0]
#del row
#del cursor



#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#fc = "airports.shp"
#delimitedField = arcpy.AddFieldDelimiters(fc,"COUNTY")
#cursor = arcpy.da.SearchCursor(fc, ["NAME"], delimitedField + " = 'Anchorage Borough'")
#for row in cursor:
#    print row[0]
#del row
#del cursor



#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#infc = "airports.shp"
#outfc = "Results/airports_anchorage.shp"
#delimitedfield = arcpy.AddFieldDelimiters(infc, "COUNTY")
#arcpy.Select_analysis(infc, outfc, delimitedfield + " ='Anchorage Borough'")




#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#fc = "Results/airports.shp"
#delimfield = arcpy.AddFieldDelimiters(fc, "STATE")
#cursor = arcpy.da.UpdateCursor(fc, ["STATE"], delimfield + " <> 'AK'")
#for row in cursor:
#    row[0] = "AK"
#    cursor.updateRow(row)
#del row
#del cursor

#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#fc = "Results/airports.shp"
#cursor = arcpy.da.UpdateCursor(fc, ["TOP_ENP"])
#for row in cursor:
#    if row[0] < 100000:
#        cursor.deleteRow()
#del row
#del cursor








                            ###Exercise7
#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#sg11 = "\"FEATURE\" = 'Airport'"
#sg12 = "\"FEATURE\" = 'Seaplane Base'"
#arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp", sq11)
#arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp", sq12)
#arcpy.Buffer_analysis("Results/airports_final.shp", "Results/aiports_buffers.shp", "15000 METERS")
#arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_buffers.shp", "7500 METERS")

#import arcpy
#from arcpy import env
#env.workspace = "G:/Exercise for Python/Python/Data/Exercise07"
#fc = "roads.shp"
#arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
#cursor = arcpy.da.UpdateCursor(fc,["FEATURE", "FERRY"])
#for row in cursor:
#    if row[0] == "Ferry Crossing":
#        row[1] = "YES"
#    else:
#        row[1] = "NO"
#    cursor.UpdateRow(row)
