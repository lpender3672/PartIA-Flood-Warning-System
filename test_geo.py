
from distutils.command.build import build
from re import A
from socket import AI_PASSIVE
from floodsystem.station import MonitoringStation

from floodsystem.stationdata import build_station_list

from floodsystem.geo import *


def test_stations_by_distance(): # get a list of tuples of (station class, distance to p) sorted by distance to p
    ds = "dummy string"

    closer_coord = (0, 1.0)
    further_coord = (0, 2.0)

 
    closer = MonitoringStation(ds, ds, "Closer_Station", closer_coord, (0, 0), ds, ds)
    further = MonitoringStation(ds, ds, "Further_Station", further_coord, (0, 0), ds, ds)

    sorted_stations = stations_by_distance([closer, further], (0,0))

    assert sorted_stations[0][0].name == closer.name
    assert sorted_stations[1][0].name == further.name


def test_stations_within_radius():
    ds = "dummy string"

    closer_coord = (0, 1.0)
    further_coord = (0, 2.0)

 
    closer = MonitoringStation(ds, ds, "Closer_Station", closer_coord, (0, 0), ds, ds)
    further = MonitoringStation(ds, ds, "Further_Station", further_coord, (0, 0), ds, ds)

    filtered_stations = stations_within_radius([closer, further], (0,0), 112)

    assert len(filtered_stations) == 1
    

def test_rivers_with_station():
    ds = "dummy string"

    river_station = MonitoringStation(ds, ds, ds, (0,0), (0, 0), "river test", ds)

    rivers = rivers_with_station([river_station])

    assert rivers[0] == "river test"    

def test_stations_by_river():
    ds = "dummy string"

    river1_station1 = MonitoringStation(ds, ds, ds, (0,0), (0, 0), "river 1", ds)
    river1_station2 = MonitoringStation(ds, ds, ds, (0,0), (0, 0), "river 1", ds)
    river2_station3 = MonitoringStation(ds, ds, ds, (0,0), (0, 0), "river 2", ds)

    river_to_stations = stations_by_river([river1_station1, river1_station2, river2_station3])

    assert len(river_to_stations["river 1"]) == 2
    assert len(river_to_stations["river 2"]) == 1


def test_rivers_by_station_number():
    
    
    pass
