with open('input', 'r') as input_file:
    data = [(d, int(x)) for d, x in map(str.split, input_file.readlines())]

pos, depth = 0, 0
for entry in data:
    match entry:
        case 'forward', x:
            pos += x
        case 'up', x:
            depth -= x
        case 'down', x:
            depth += x

print(f"{pos} * {depth} = {pos * depth}")
