with open('input', 'r') as input_file:
    start_pos = list(map(int, input_file.readline().split(',')))

min = min(start_pos)
max = max(start_pos)

min_fuel = max * len(start_pos)
for dest in range(min, max + 1):
    fuel = 0
    for pos in start_pos:
        fuel += abs(pos - dest)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
