from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import categorised_flood_risk
from floodsystem.stationdata import build_station_list,update_water_levels

"""Unit test for the flood module"""

def test_for_stations_level_over_threshhold():    
    ds = 'dummy string'

    #Creating dummy monitoring stations for testing, note tha s3 has inconsistent range
    s1 = MonitoringStation(ds,ds,ds,ds,(0,1),ds,ds)
    s2 = MonitoringStation(ds,ds,ds,ds,(0,1),ds,ds)
    s3 = MonitoringStation(ds,ds,ds,ds,(1,0),ds,ds)
    s4 = MonitoringStation(ds,ds,ds,ds,(0,1),ds,ds)
    s5 = MonitoringStation(ds,ds,ds,ds,(0,1),ds,ds)

    #Range chosen such that latest level will be equal to relative water level
    s1.latest_level = 0.8 
    s2.latest_level = 0.4
    s3.latest_level = 0.6
    s4.latest_level = 0.7
    s5.latest_level = 0.1

    stations = [s1, s2, s3, s4, s5]

    test = stations_level_over_threshold(stations, 0.2)

    #Expected output is a list of tuples
    #Expected ouput does not include s3(inconsistent range) and does not include s5(relative water level below threshold)
    #Expected output has s1, s4, s2 in decending order of relative water level 
    assert test == [(s1, 0.8), (s4, 0.7), (s2, 0.4)]


def test_for_categorized_flood_risk():
    stations = build_station_list()
    update_water_levels(stations)
    # This is how low warning stations are initally defined. Procedures are perfomed to move items from low warning list into other catagories.
    test_low = stations_level_over_threshold(stations,0.8)
    # The sum of lengths of all the categories must add up to the intial low warning list, this shows that each station is accounted for.
    faulty,low,moderate,high,severe = categorised_flood_risk(stations)
    assert len(faulty) + len(low) + len(moderate) + len(high) + len(severe) == len(test_low)