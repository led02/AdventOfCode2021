with open('input', 'r') as input_file:
    start_pos = list(map(int, input_file.readline().split(',')))

min = min(start_pos)
max = max(start_pos)

min_fuel = max**2 * len(start_pos)
for dest in range(min, max + 1):
    fuel = 0
    for pos in start_pos:
        delta = abs(pos - dest)
        fuel += (delta * (delta + 1)) // 2
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
