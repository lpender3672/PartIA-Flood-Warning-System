# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
import math
from reprlib import recursive_repr
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def distance_between_coords(p1,p2):
    """Function to get circumfurential distance in KM between two lat, long coordinates using Haversine's equation

    Args:
        p1 (list): first lat, long coordinates
        p2 (list): second lat, long coordinates

    """

    k = math.pi/180  # conversion factor into radians

    lon1 = p1[1] * k
    lon2 = p2[1] * k
    lat1 = p1[0] * k
    lat2 = p2[0] * k

    a = math.sin(( lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin( (lon2 - lon1) / 2)**2
    c = 2 * math.asin( math.sqrt(a) ) # Haversine formula
    
    # Radius of earth in kilometers.
    r = 6371
      
    return(c * r)

def stations_by_distance(stations, p): # get a list of tuples of (station class, distance to p) sorted by distance to p
    """Function to get a list of tuples of (station class, distance to p) sorted by distance to point p

    Args:
        stations ([MonitoringStation]): List of stations
        p ([float]): lat, long coordinates

    Returns:
        [tuple]: (station, distance to p from station)
    """
    
    station_distances = []
    for s in stations:
        d = distance_between_coords(s.coord, p)
        station_distances.append((s,d))

    distance_from_tuple = lambda x : x[1] # key used by sorted to get the distance from the tuple (station, distance)
    sorted_station_distances = sorted(station_distances, key = distance_from_tuple) # sorting using key

    return sorted_station_distances


def stations_within_radius(stations, centre, r):
    """Function to get a list of stations within radius r

    Args:
        stations ([MonitoringStation]): List of stations
        centre ([float]): lat, long coordinates
        r ([type]): Maximum circumfurential distance between station and centre in KM

    Returns:
        [MonitoringStation]: [description]
    """

    sorted_stations = stations_by_distance(stations, centre) # gets stations with distance to centre sorted already

    stations_in_radius = []
    for s,d in sorted_stations:
        if d < r:
            stations_in_radius.append(s)
        else:   # dont need to check any more radaii as they are sorted
            break
    
    return stations_in_radius


def rivers_with_station(stations):
    """Function to get list of rivers with a station

    Args:
        stations ([MonitoringStation]): List of stations

    Returns:
        [string]: list of rivers with a station
    """

    rivers = []

    for s in stations:
        if s.river not in rivers: # if its not already in rivers
            rivers.append(s.river) # add to rivers

    return rivers

def stations_by_river(stations):
    """Function to get a dict that maps river names to a list of station objects on a given river. The function should have the

    Args:
        stations ([MonitoringStation]): List of stations

    Returns:
        {string : [MonitoringStation]}: dict of river names mapped to a list of stations on that river
    """

    rivers = rivers_with_station(stations)

    river_stations = {}
    
    for r in rivers:
        river_stations[r] = []

    for s in stations:
        
        river_stations[s.river].append(s)

    return river_stations


def rivers_by_station_number(stations, N):

    """Function to get the N rivers with the greatest number of monitoring stations. 

    Args:
        stations ([MonitoringStation]): List of stations
        N (int): Minimum number of rivers

    Returns:
        [tuple]: list of tuples of form (river name, number of stations), sorted by the number of stations
    """

    
    rivers = [] #creating list for all rivers
    
    for s in stations:
        rivers.append(s.river)
    
    testing = rivers_with_station(stations) #Considering only rivers with stations we create list of tuples contatining each river once and how many stations it has
    
    river_with_counter = []
    
    for i in testing:
        river_with_counter.append((i,rivers.count(i)))
    
    count = 0 
    
    final = [(0,0)]
    

    while count < N-1: # While the position number is under what is required we search the list finding the max and append it to second list of tuples to be returned
            max1 = 0 

            for j in range(len(river_with_counter)):
                if river_with_counter[j][1] >= max1:
                    max1 = river_with_counter[j][1]
                    k = j 

            if max1 < final[-1][1]:
                count += 1 
            
            final.append((river_with_counter[k][0], max1))

            river_with_counter.remove(river_with_counter[k])
        
    for l in range(len(river_with_counter)): # Catching any rivers with the same number of stations as the final river in the list to be returned
        if river_with_counter[l][1] == max1:
            final.append(river_with_counter[l])
        
    final.remove(final[0])

    return final

