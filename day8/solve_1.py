with open('input', 'r') as input_file:
    output = [
        tail.strip().split(' ')
        for _, tail in map(lambda s: s.split(' | '), input_file.readlines())
    ]

ctr = 0
for display in output:
    for digit in display:
        if len(digit) in (2, 3, 4, 7):
            ctr += 1

print(ctr)
