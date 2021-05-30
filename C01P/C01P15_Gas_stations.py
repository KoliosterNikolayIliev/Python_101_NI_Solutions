def gas_stations(distance, tank_size, stations):
    pass


tests = [
    gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [80, 140, 220, 290],
    gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) == [70, 140, 210, 280, 350],
    gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]) == [40, 80],
    gas_stations(100, 50, [10, 90]) == [],
]
for test in tests:
    print(test)
