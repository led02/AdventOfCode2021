with open('input', 'r') as input_file:
    data = [list(map(int, line.strip())) for line in input_file.readlines()]

def get_stencil(map_data, x, y):
    stencil = []
    if y > 0:
        stencil.append((map_data[y - 1][x], x, y - 1))
    if y < len(map_data) - 1:
        stencil.append((map_data[y + 1][x], x, y + 1))
    if x > 0:
        stencil.append((map_data[y][x - 1], x - 1, y))
    if x < len(map_data[y]) - 1:
        stencil.append((map_data[y][x + 1], x + 1, y))
    return stencil

def find_basin(map_data, x, y):
    points_added = [(x, y)]
    basin = [(map_data[y][x], x, y)]
    while points_added:
        new_points = points_added[:]
        points_added = []
        for point in new_points:
            x, y = point
            stencil = get_stencil(map_data, x, y)
            for a, x_a, y_a in stencil:
                if a == 9:
                    continue
                if a >= map_data[y][x]:
                    basin.append((a, x_a, y_a))
                    points_added.append((x_a, y_a))
    return basin

basins = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if all(map(lambda a: a[0] > data[y][x], get_stencil(data, x, y))):
            basins.append(find_basin(data, x, y))

def print_map(map_data, basins):
    basin_map = [[' '] * len(row) for row in map_data]
    for basin in basins:
        for a, x, y in basin:
            basin_map[y][x] = str(a)

    print('\n'.join(''.join(row) for row in basin_map))

print_map(map_data, basins)
i, j, k = sorted(map(len, basins), reverse=True)[:3]
print(i * j * k)
