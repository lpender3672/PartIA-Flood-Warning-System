
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib
from floodsystem.analysis import polyfit
import datetime


def stations_level_over_threshold(stations, tol):
    '''Function that retuns a list of tuples containing stations and their relative water level for stations above a tolerance level sorted by 
    the magnitude of their relative water level (highest first)'''
    unsorted = [ ( i , i.relative_water_level() ) for i in stations if i.relative_water_level() != None and i.relative_water_level() > tol ]
    return sorted(unsorted, key = lambda x: x[1], reverse = True)


def stations_highest_rel_level(stations, N):
    """function that returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest
        Sorted in descending order by relative level
    
    Args:
        stations (list): list of stations
        N (int): number of most at risk stations
    """

    return stations_level_over_threshold(stations, 0)[0:N]
        

def categorised_flood_risk(stations):
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
    
    return(faulty, low, moderate, high, severe)