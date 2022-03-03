from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

import datetime

def run():

    dt = 5 # past 5 days
    error_counter = 0


    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    most_at_risk = stations_highest_rel_level(stations, 6) #6 stations with highest level accounting for faulty stations

    counter = 0
    while counter < 5:
        for s,r in most_at_risk:
            dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))
            try:
                dates[-1]
                print(most_at_risk)
                plot_water_levels(s, dates, levels)
                counter += 1
            except:
                pass
    


if __name__ == "__main__":
    run()