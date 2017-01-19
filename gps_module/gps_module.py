
import mlpux
import json
import numpy as np
import random
"""
A fake module which will be used for unit testing the demo framework.

Here, I'll slowly accumulate a list of possible demo architectures to run through
the demo framework.
"""

@mlpux.Interactive()
@mlpux.Demo()
def generate_gps_list(num=2,lat_var=90./10000., lon_var=180./10000.):
    """
    Generate gaussian distribution of GPS coordinates around a central
    point. If no central point is supplied, 
    
    param center: tuple (lat,long)
    param lat_var: variance of points generated in lattitude
    param long_va: varience of points generated in longitude
    """
    sign = np.array([-1,1])
    
    center = (random.uniform(-90.,90.), random.uniform(-180.,180.))
    list_of_list_pairs = []
    list_of_tuples = []
    lat_list = []
    lon_list = []
    for i in range(num):
        lat = np.random.normal(loc=center[0], scale=lat_var**(0.5))
        lon = np.random.normal(loc=center[1], scale=lon_var**(0.5))
        list_of_list_pairs.append([lat,lon])
        list_of_tuples.append((lat,lon))
        lat_list.append(lat)
        lon_list.append(lon)
    return list_of_tuples
