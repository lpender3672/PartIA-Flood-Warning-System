from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():

    stations = build_station_list() # get stations


    rivers = rivers_with_station(stations)
    print(f"there are {len(rivers)} rivers with stations")
    print(sorted(rivers)[:10])

    river_stations = stations_by_river(stations)

    sampled_rivers = ["River Aire", "River Cam", "River Thames"]

    for r in sampled_rivers:
        station_names = []
        for s in river_stations[r]:
            station_names.append(s.name)
        
        print(sorted(station_names))



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()