import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    
    '''This function creates a least-squares polynomial fit of degree to water level data given'''

    datetime_shift = 1
    dates_num = matplotlib.dates.date2num(dates)
    coeff = np.polyfit(dates_num - dates_num[datetime_shift - 1], levels, p)
    poly = np.poly1d(coeff)

    return(poly, datetime_shift)
