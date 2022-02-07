
from socket import AI_PASSIVE
from floodsystem.station import MonitoringStation

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
    pass


def test_rivers_with_station():
    pass

def test_stations_by_river():
    pass

def test_rivers_by_station_number():
    pass


