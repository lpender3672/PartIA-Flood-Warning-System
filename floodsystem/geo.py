# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
from argparse import ArgumentError
import math
from reprlib import recursive_repr

from floodsystem.station import MonitoringStation
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

    if (type(p1) not in [tuple, list]) or len(p1) != 2:
        raise ArgumentError(f"p1 is of type {type(p1)}. Expected tuple or list")
    if (type(p2) not in [tuple, list]) or len(p1) != 2:
        raise ArgumentError(f"p2 is of type {type(p2)}. Expected tuple or list")


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

    if type(stations) != list:
        raise ArgumentError(f"stations expected to be of type list, not of the type {type(stations)}")
    if not all([type(x) == MonitoringStation for x in stations]):
        raise ArgumentError("stations must be a list of the MonitoringStation object")

    if (type(p) not in [list, tuple]) or len(p) != 2:
        raise ArgumentError(f"p expected to be of type list or tuple of length 2, not of the type {type(p)}")
    
    
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

    if type(stations) != list:
        raise ArgumentError(f"stations expected to be of type list, not of the type {type(stations)}")
    if not all([type(x) == MonitoringStation for x in stations]):
        raise ArgumentError("stations must be a list of the MonitoringStation object")

    if (type(centre) not in [list, tuple]) or len(centre) != 2:
        raise ArgumentError(f"centre expected to be of type list or tuple of length 2, not of the type {type(centre)}")

    if (type(r) not in [float, int]) or r <= 0:
        raise ArgumentError(f"r expected to be of type float or int where r > 0")

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
    if type(stations) != list:
        raise ArgumentError(f"stations expected to be of type list, not of the type {type(stations)}")
    if not all([type(x) == MonitoringStation for x in stations]):
        raise ArgumentError("stations must be a list of the MonitoringStation object")


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

    if type(stations) != list:
        raise ArgumentError(f"stations expected to be of type list, not of the type {type(stations)}")
    if not all([type(x) == MonitoringStation for x in stations]):
        raise ArgumentError("stations must be a list of the MonitoringStation object")

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

    if type(stations) != list:
        raise ArgumentError(f"stations expected to be of type list, not of the type {type(stations)}")
    if not all([type(x) == MonitoringStation for x in stations]):
        raise ArgumentError("stations must be a list of the MonitoringStation object")
    if type(N) != int or N <= 0:
        raise ArgumentError("N should be of type int, where N > 0")

    
    rivers_mapped_to_stations = stations_by_river(stations)

    get_length_of_stations = lambda x: len(x[1])
    rivers_sorted_by_N_stations = dict(sorted(rivers_mapped_to_stations.items(), key = get_length_of_stations, reverse=True))

    l = []
    for name,river_stations in rivers_sorted_by_N_stations.items():
        n_rivers = len(river_stations)

        if len(l) < N or l[-1][1] == n_rivers:
            l.append( (name, n_rivers ) )
        else:
            break

    return l
    
    
