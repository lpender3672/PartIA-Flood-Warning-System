from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels, fetch_dates_measure_levels

import datetime

def run():

    dt = 5 # past 5 days


    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    risk_sorted_stations = stations_level_over_threshold(stations, 0)

    nstations = 0

    for s,r in risk_sorted_stations:
        # dates, levels = fetch_measure_levels(s.measure_id, dt=datetime.timedelta(days=dt))
        dates, levels = fetch_dates_measure_levels(s.measure_id, datetime.datetime.utcnow())

        if bool(dates) and nstations < 5:
            plot_water_level_with_fit(s, dates, levels, 4)
            nstations += 1
        
        elif nstations >= 5:
            break



if __name__ == "__main__":
    run()