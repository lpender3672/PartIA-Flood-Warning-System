from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():

    stations = build_station_list() # get stations

    cambridge_coord =  (52.2053, 0.1218)

    distance_sorted_stations = stations_by_distance(stations, cambridge_coord) # get distance sorted stations

    #(station name, town, distance)
    print("Closest Stations to Cambridge")
    closest = []
    for s,d in distance_sorted_stations[:10]: # loop through the first 10
        closest.append( (s.name, s.town, d) ) # append a new tuple containing name, town, distance
    print(closest)

    print("Furthest Stations to Cambridge")
    furthest = []
    for s,d in distance_sorted_stations[-10:]: # loop through the last 10
        furthest.append( (s.name, s.town, d) ) # append a new tuple containing name, town, distance
    print(furthest)

    



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
