from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    most_at_risk = stations_highest_rel_level(stations, 10)

    for s,r in most_at_risk:
        print(s.name, r)



if __name__ == "__main__":
    run()