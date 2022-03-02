from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit
import datetime
from datetime import timedelta

#stations = build_station_list()

#update_water_levels(stations)
#dt = 3
#warned = []
#for i in stations:

    #if type(i.relative_water_level()) == float and i.relative_water_level() > 1:
        #dates,levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days= dt))
        #avgrad = (levels[0] - levels[-1])/288
        #weeklevel = levels[0] + avgrad*6272
        #if weeklevel > 2:
            #warned.append([i.name,weeklevel])

#print(warned)




stations = build_station_list()
update_water_levels(stations)
risk_sorted_stations = stations_level_over_threshold(stations, 0)

station = risk_sorted_stations[3][0]

p = 3
dates,levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days= 1))
poly,d0 = polyfit(dates, levels, p)
future_T = datetime.datetime.now() - datetime.timedelta(days=1)
future_N = matplotlib.dates.date2num(future_T)

offset = matplotlib.dates.date2num(dates[0])
level = poly(future_N - offset)


print(station.name)
print((level - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0]))
print(level)
