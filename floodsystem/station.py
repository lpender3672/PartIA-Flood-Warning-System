# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
    
    def typical_range_consistent(self):
        """ Determines if the typical range is consistent

        Returns:
            bool: is the range consistent
        """
        
        if type(self.typical_range) != tuple or (self.typical_range[0] > self.typical_range[1]) or (self.typical_range[0] == 0 and self.typical_range[1] ==0):
            return False
        else:
            return True
    
    
    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

def inconsistent_typical_range_stations(stations):
    """Returns a list of stations that have inconsistent data

    Args:
        stations ([type]): [description]

    Returns:
        [MonitoringStation]: list of monitoring stations with inconsistant ranges
    """

    if type(stations) != list:
        raise ArgumentError(f"stations expected to be of type list, not of the type {type(stations)}")
    if not all([type(x) == MonitoringStation for x in stations]):
        raise ArgumentError("stations must be a list of the MonitoringStation object")


    inconsistent = []
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent.append(station)
    return(inconsistent)


