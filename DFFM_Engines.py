
# coding: utf-8

# In[88]:


# Import libraries
from arcgis.gis import GIS
import urllib.request, csv
from arcgis import features
import pandas as pd
import os


# In[89]:


# Connect to the GIS
gis = GIS("https://www.arcgis.com", "YOUR AGOL USERNAME HERE", " YOUR AGOL PASSWORD HERE")
print("Logged in as " + str(gis.properties.user.username))


# ## Overwrite the feature layer
# Let us overwrite the feature layer using the new csv file we just created. To overwrite, we will use the `overwrite()` method.

# In[90]:


#item id of the feature layer in AGOL Organization
Engines_featureLayer_item = gis.content.get('Enter Feature Layer ID Here')


# In[91]:


from arcgis.features import FeatureLayerCollection
Engines_flayer_collection = FeatureLayerCollection.fromitem(Engines_featureLayer_item)


# ### Access the overwritten feature layer
# Let us query the feature layer and verify the number of features has increased to `51`.

# In[92]:


#call the overwrite() method which can be accessed using the manager property
Engines_flayer_collection.manager.overwrite('DFFM_Engines.csv (file location)')


# In[93]:


Engines_incidents_flayer = Engines_featureLayer_item.layers[0] #there is only 1 layer
Engines_incidents_flayer.query(return_count_only=True) #get the total number of features


# In[96]:


dirPath = "(file location where 'DFFM_Engines.csv' is located"
fileList = os.listdir(dirPath)
for fileName in fileList:
 os.remove(dirPath+"/"+fileName)
 print("file deleted")
