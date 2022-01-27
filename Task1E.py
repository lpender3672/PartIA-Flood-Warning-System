from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
   
    print('Printing tuple list of rivers with the most stations. Rivers with the same number of stations are included.')
    
    print(rivers_by_station_number(stations,9))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()