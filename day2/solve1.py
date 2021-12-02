pos = 0
depth = 0

with open('input', 'r') as input_file:
    for entry in map(str.split, input_file.readlines()):
        match entry:
            case 'forward', x:
                pos += int(x)
            case 'up', x:
                depth -= int(x)
            case 'down', x:
                depth += int(x)

print(pos * depth)
