with open('input', 'r') as input_file:
    data = [l.strip().split(' -> ') for l in input_file.readlines()]

points = []
max_x, max_y = 0, 0
for p0, p1 in data:
    p0 = tuple(map(int, p0.split(',')))
    p1 = tuple(map(int, p1.split(',')))
    max_x = max(p0[0], p1[0], max_x)
    max_y = max(p0[1], p1[1], max_y)
    points.append((p0, p1))

vent_map = [[0] * (max_x + 1) for _ in range(max_y + 1)]

for (x0, y0), (x1, y1) in points:
    if x0 == x1:
        if y0 > y1: y0, y1 = y1, y0
        for y in range(y0, y1 + 1):
            vent_map[y][x0] += 1

    elif y0 == y1:
        if x0 > x1: x0, x1 = x1, x0
        for x in range(x0, x1 + 1):
            vent_map[y0][x] += 1

    else:
        if x0 > x1: x0, x1, y0, y1 = x1, x0, y1, y0
        s = 1 if y0 < y1 else -1
        for d in range(x1 - x0 + 1):
            vent_map[y0 + s * d][x0 + d] += 1

count = sum(sum(map(lambda v: v >= 2, row)) for row in vent_map)
print(count)
