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
    dy = p1[1] - p2[1]

    return math.sqrt(dx**2 + dy**2)

def stations_by_distance(stations, p):
    
    station_distances = []
    for s in stations:
        d = distance_between_points(s.coord, p)
        station_distances.append((s,d))

    index_tuple = lambda x : x[1]
    sorted_station_distances = sorted(station_distances, key = index_tuple)

    return sorted_station_distances
