# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
import math
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def distance_between_points(p1,p2):

    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]  # absolute coordinates to relative coordinates

    return math.sqrt(dx**2 + dy**2) # pythagorous 

def stations_by_distance(stations, p): # get a list of tuples of (station class, distance to p) sorted by distance to p
    
    station_distances = []
    for s in stations:
        d = distance_between_points(s.coord, p)
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
    