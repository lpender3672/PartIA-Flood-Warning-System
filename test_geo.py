
from socket import AI_PASSIVE
from floodsystem.station import MonitoringStation

from floodsystem.geo import *


def test_stations_by_distance(): # get a list of tuples of (station class, distance to p) sorted by distance to p
    ds = "dummy string"

    closer_coord = (0, 1.0)
    further_coord = (0, 2.0)

 
    closer = MonitoringStation("Closer_Station", ds, ds, closer_coord, (0, 0), ds, ds)
    further = MonitoringStation("Further_Station", ds, ds, further_coord, (0, 0), ds, ds)

    sorted_stations = stations_by_distance([closer, further], (0,0))

    assert sorted_stations[0].id == closer.id
    assert sorted_stations[1].id == further.id


def test_stations_within_radius():
    pass


def test_rivers_with_station():
    pass

def test_stations_by_river():
    pass

def test_rivers_by_station_number():
    pass


