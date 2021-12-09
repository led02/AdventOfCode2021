with open('input', 'r') as input_file:
    data = [list(map(int, line.strip())) for line in input_file.readlines()]

def get_stencil(map_data, x, y):
    stencil = []
    if y > 0:
        stencil.append(map_data[y - 1][x])
    if y < len(map_data) - 1:
        stencil.append(map_data[y + 1][x])
    if x > 0:
        stencil.append(map_data[y][x - 1])
    if x < len(map_data[y]) - 1:
        stencil.append(map_data[y][x + 1])
    return stencil

risk_sum = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if all(map(lambda a: a > data[y][x], get_stencil(data, x, y))):
            risk_sum += data[y][x] + 1

print(risk_sum)
