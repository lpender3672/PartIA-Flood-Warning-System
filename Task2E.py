from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

import datetime

def run():

    dt = 5 # past 5 days


    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    most_at_risk = stations_highest_rel_level(stations, 5) # 5 most at risk stations

    for s,r in most_at_risk:
        
        dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))

        print(most_at_risk)
        plot_water_levels(s, dates, levels)



if __name__ == "__main__":
    run()