import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
#import contextily as ctx 
import geopandas as gpd 
import os 
df = gpd.read_file('./us_eco_l3_state_boundaries/us_eco_l3_state_boundaries.shp')
df = df.to_crs("EPSG:4326")
df.boundary.plot()
plt.show()
print(df.iloc[0,:])