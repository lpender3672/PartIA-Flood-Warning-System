import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    """Displays a graph of a stations water levels over time

    Args:
        station (MonitoringStation): _description_
        dates (list): list of DateTime objects representing time point
        levels (list): list of floats representing water level point
    """

    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    
    plt.show()


