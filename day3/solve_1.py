with open('input', 'r') as input_file:
    data = [tuple(map(int, v.strip())) for v in input_file.readlines()]

sums = list(map(sum, zip(*data)))

delta = int(''.join(map(lambda s: str(int(s > len(data) / 2)), sums)), base=2)
gamma = int(''.join(map(lambda s: str(int(s < len(data) / 2)), sums)), base=2)
print(f'{delta} * {gamma} = {delta * gamma}')
