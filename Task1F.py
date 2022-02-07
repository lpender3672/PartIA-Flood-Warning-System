from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    x = inconsistent_typical_range_stations(stations)
    inconsistent_station_names = []
    for i in x:
        inconsistent_station_names.append(i.name)
    print(inconsistent_station_names)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()