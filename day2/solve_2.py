with open('input', 'r') as input_file:
    data = [(d, int(x)) for d, x in map(str.split, input_file.readlines())]

aim, pos, depth = 0, 0, 0
for entry in data:
    match entry:
        case 'forward', x:
            pos += x
            depth += aim * x
        case 'up', x:
            aim -= x
        case 'down', x:
            aim += x

print(f"{pos} * {depth} = {pos * depth}")
