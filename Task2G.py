from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import categorised_flood_risk


stations = build_station_list()
update_water_levels(stations)


faulty,low,moderate,high,severe = categorised_flood_risk(stations)

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
