


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
        
