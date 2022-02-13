from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    # Uses function stations_level_over_threshold to print station name and relative water level for stations above 0.8 relative water level (decending order)
    for i in stations_level_over_threshold(stations,0.8):
        print(i[0].name + '  ' + str(i[1]))

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
