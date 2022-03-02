from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit
import datetime



stations = build_station_list()
update_water_levels(stations)

low = stations_level_over_threshold(stations,0.8)
moderate = stations_level_over_threshold(stations, 1)
high = []
severe = []
faulty = []

dt = 1
for i in range(0, len(moderate)-1):
    dates,levels = fetch_measure_levels(moderate[i][0].measure_id, dt=datetime.timedelta(days=dt))
    try:
        A = levels[-1]
        B = levels[0]
        if B - A > 0.3:
            if moderate[i][0].typical_range_consistent():
                p = 3
                poly,d0 = polyfit(dates, levels, p)
                future_T = datetime.datetime.now() - datetime.timedelta(days=2)
                future_N = matplotlib.dates.date2num(future_T)
                offset = matplotlib.dates.date2num(dates[0])
                level = poly(future_N - offset)
                rel_level = (level - moderate[i][0].typical_range[0])/(moderate[i][0].typical_range[1]-moderate[i][0].typical_range[0])
                if rel_level > 1.5:
                    severe.append(moderate[i])
                else:
                    high.append(moderate[i])
            else:
                high.append(moderate[i])


    except IndexError:
        faulty.append(moderate[i])

print(len(low))
low = [x for x in low if x not in moderate]
moderate  = [x for x in moderate if x not in faulty]
moderate  = [x for x in moderate if x not in high]
moderate  = [x for x in moderate if x not in severe]
print(len(faulty))
print(len(low))
print(len(moderate))
print(len(high))
print(len(severe))

print('FAULTY')
print([i[0].name for i in faulty])
print('LOW')
print([i[0].name for i in low])
print('MODERATE')
print([i[0].name for i in moderate])
print('HIGH')
print([i[0].name for i in high])
print('SEVERE')
print([i[0].name for i in severe])

