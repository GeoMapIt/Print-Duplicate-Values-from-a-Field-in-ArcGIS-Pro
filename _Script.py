'''
Created by Nathan R
Used to quickly print duplicate values from a feature layer

To use, run within ArcGIS's built in Python Terminal
'''

def unique_values(table, field):
    import collections
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({row[0] for row in cursor})

data_path = r'Containment_Calculations' #Any shapefile, feature class, or table
field_name = 'Tank' #Field to be checked

myValues = unique_values(data_path, field_name)
print (str(len(myValues)) + " unique values")


with arcpy.da.SearchCursor(data_path, field_name) as cursor:
    uniqueList = []
    for row in cursor:
        if row in uniqueList:
            print (str(row) + " is a duplicate")
        else:
            uniqueList.append(row)
