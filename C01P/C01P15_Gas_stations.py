# This one is watch, copy driven development

def gas_stations(distance, tank_size, stations):
    result = []

    stations_with_target = [x for x in stations if x < distance] + [distance]
    diffs = [stations_with_target[0]]

    for index in range(0, len(stations_with_target) - 1):
        diffs.append(stations_with_target[index + 1] - stations_with_target[index])

    current_tank_size = tank_size

    for index, diff, in enumerate(diffs):
        current_tank_size -= diff

        if current_tank_size <= 0:
            current_tank_size = tank_size - diff

            if current_tank_size <= 0:
                return []

            result.append(stations[index - 1])

    return result


tests = [
    gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [80, 140, 220, 290],
    gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) == [70, 140, 210, 280, 350],
    gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]) == [40, 80],
    gas_stations(100, 50, [10, 90]) == [],
]
for test in tests:
    print(test)
