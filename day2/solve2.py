aim = 0
pos = 0
depth = 0

with open('input', 'r') as input_file:
    for entry in map(str.split, input_file.readlines()):
        match entry:
            case 'forward', x:
                pos += int(x)
                depth += aim * int(x)
            case 'up', x:
                aim -= int(x)
            case 'down', x:
                aim += int(x)

print(pos * depth)
