from floodsystem.geo import rivers_with_station, rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    print('Printing list of (river, number of stations) tuples for the 9 rivers with the most stations')
    print(rivers_by_station_number(stations,9))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()