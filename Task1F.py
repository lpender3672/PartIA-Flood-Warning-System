from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():

    print('Printing all stations with inconsistent typical range data in alphabetical order:')
 
    stations = build_station_list()

    return sorted(inconsistent_typical_range_stations(stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()