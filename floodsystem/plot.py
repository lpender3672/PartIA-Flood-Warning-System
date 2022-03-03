import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta

import numpy as np
from .analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Displays a graph of a stations water levels over time

    Args:
        station (MonitoringStation): _description_
        dates (list): list of DateTime objects representing time point
        levels (list): list of floats representing water level point
    """

    plt.plot(dates, levels)


    typical_mins = np.full(len(dates), station.typical_range[0])
    typical_maxs = np.full(len(dates), station.typical_range[1])
    plt.plot(dates, typical_mins, label = "Typical minimum level")
    plt.plot(dates, typical_maxs, label = "Typical maximum level")

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    
    plt.legend()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    '''This function plots a graph of water levels over a period of time for a certain station, along with its least-squares polynomial fit'''
    
    poly, d0 = polyfit(dates, levels, p)
    dates_num = matplotlib.dates.date2num(dates)
    print(type(dates_num))

    typical_mins = np.full(len(dates), station.typical_range[0])
    typical_maxs = np.full(len(dates), station.typical_range[1])

    plt.plot(dates, levels, label = "Real data")
    plt.plot(dates, poly(dates_num - dates_num[d0 - 1]), label = "Least-squares polynomial fit")
    plt.plot(dates, typical_mins, label = "Typical minimum level")
    plt.plot(dates, typical_maxs, label = "Typical maximum level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()
    plt.tight_layout()  
    plt.show()

        
        

