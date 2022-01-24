from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():

    City_Centre = (52.2053, 0.1218)
    Radius = 10

    stations = build_station_list() # get stations
    stations_in_radius = stations_within_radius(stations, City_Centre, Radius ) # get stations in radius

    station_names = []
    for s in stations_in_radius:
        station_names.append(s.name) # get list of station names in radius

    sorted_stations = sorted(station_names) # sort alphabetically

    print(sorted_stations)
    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()