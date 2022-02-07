
from distutils.command.build import build
from re import A
from socket import AI_PASSIVE
from floodsystem.station import MonitoringStation

from floodsystem.stationdata import build_station_list
import random
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
    stations = build_station_list()
    #Creatng the rivers by station number list of tuples for the n highest number of stations per river where n is a random number from 1, 10 (rand_num)
    rand_num = random.randint(1,10)
    x = rivers_by_station_number(stations, rand_num)
    #The function should return a list
    assert type(x) == list
    #The list should contain tuples
    assert type(x[rand_num//2]) == tuple
    #The rivers should be in order of most stations to least stations
    for i in range(1,len(x)):
        assert x[i-1][1] >= x[i][1]
    #The list of tuples should be the same length or greater than rand_num allowing for the printing of rivers with the same number stations
    assert len(x) >= rand_num 
