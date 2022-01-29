from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():

    print('Printing all stations with inconsistent typical range data in alphabetical order:')
 
    stations = build_station_list()

    x = inconsistent_typical_range_stations(stations)

    name_list = []

    for i in x:
        name_list.append(i.name)
    
    print(sorted(name_list))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()