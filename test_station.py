# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *
from floodsystem.stationdata import build_station_list


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    #Build station list to test on
    stations = build_station_list()
    #Produce the list of inconsistent monitoring stations
    x = inconsistent_typical_range_stations(stations)
    #The function should return a list
    assert type(x) == list
    #The length of the list of stations with inconsistent range data should be smaller than the total list of stations
    assert len(x) < len(stations)
    #The list produced should contain only monitoring station objects
    #For the list all the typical range data should be incosistent. (type is not tuple or the lower value is greater than the upper value or both the upper and lower value are 0)
    for i in x:
        assert type(i) == MonitoringStation
        assert type(i.typical_range) != tuple or (i.typical_range[0] > i.typical_range[1]) or (i.typical_range[0] == 0 and i.typical_range[1] ==0)
    
def test_relative_water_level():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 0.57225

    assert round(s.relative_water_level(),8) == 0.5 

    trange2 = (3.4445, -2.3)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s2.latest_level = 0.57225
    
    assert s2.relative_water_level() == None

    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s3.relative_water_level() == None

    