with open('input', 'r') as input_file:
    data = [tuple(map(int, v.strip())) for v in input_file.readlines()]

def find_v(v_list, comp):
    index = 0
    while len(v_list) > 1:
        v_sum = sum(v[index] for v in v_list)
        v_filter = int(comp(v_sum, len(v_list) / 2))
        v_list = [v for v in v_list if v[index] == v_filter]
        index += 1
    return int(''.join(map(str, v_list[0])), base=2)

oxy = find_v(data[:], lambda x, y: x >= y)
co2 = find_v(data[:], lambda x, y: x < y)

print(f'{oxy} * {co2} = {oxy * co2}')
