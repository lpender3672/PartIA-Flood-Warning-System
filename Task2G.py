from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit
import datetime

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


low = stations_level_over_threshold(stations, 1)
moderate = []
dt = 1
counter = 0
for i in low:
    dates,levels = fetch_measure_levels(low[0][0].measure_id, dt=datetime.timedelta(days=dt))
    try:
        prev_lev = levels[-1]
        current_lev = levels[0]
        if current_lev > prev_lev:
            moderate.append(i)
    except:
        pass
    counter += 1 
print(counter)

#most_at_risk = stations_highest_rel_level(stations, 10)
#dt = 3
#dates,levels = fetch_measure_levels(most_at_risk[2][0].measure_id, dt=datetime.timedelta(days=dt))
#poly, d0 = polyfit(dates, levels, 3)
#dates_num = matplotlib.dates.date2num(dates)
#print(type(poly))
#print(type(d0))
#print(poly(10))
#over_level = 