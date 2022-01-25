# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
import math
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def distance_between_coords(p1,p2):

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
    
    station_distances = []
    for s in stations:
        d = distance_between_coords(s.coord, p)
        station_distances.append((s,d))

    distance_from_tuple = lambda x : x[1] # key used by sorted to get the distance from the tuple (station, distance)
    sorted_station_distances = sorted(station_distances, key = distance_from_tuple) # sorting using key

    return sorted_station_distances


def stations_within_radius(stations, centre, r):

    sorted_stations = stations_by_distance(stations, centre) # gets stations with distance to centre sorted already

    stations_in_radius = []
    for s,d in sorted_stations:
        if d < r:
            stations_in_radius.append(s)
        else:   # dont need to check any more radaii as they are sorted
            break
    
    return stations_in_radius


def rivers_with_station(stations):

    rivers = []

    for s in stations:
        if s.river not in rivers: # if its not already in rivers
            rivers.append(s.river) # add to rivers

    return rivers

def stations_by_river(stations):

    rivers = rivers_with_station(stations)

    river_stations = {}
    
    for r in rivers:
        river_stations[r] = []

    for s in stations:
        
        river_stations[s.river].append(s)

    return river_stations