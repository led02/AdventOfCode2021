with open('input', 'r') as input_file:
    data = [
        (head.strip().split(' '), tail.strip().split(' '))
        for head, tail in map(lambda s: s.split(' | '), input_file.readlines())
    ]

sum = 0
for detect, display in data:
    dmap = {}
    seg5 = []
    seg6 = []
    d1 = None
    d4 = None
    
    for digit in detect:
        digit = sorted(digit)
        
        if len(digit) == 2:
            d1 = digit
            dmap[''.join(digit)] = 1
        elif len(digit) == 3:
            dmap[''.join(digit)] = 7
        elif len(digit) == 4:
            d4 = digit
            dmap[''.join(digit)] = 4
        elif len(digit) == 5:
            seg5.append(digit)
        elif len(digit) == 6:
            seg6.append(digit)
        elif len(digit) == 7:
            dmap[''.join(digit)] = 8
        
    for digit in seg6:
        if not all(d in digit for d in d1):
            d6 = digit
            dmap[''.join(digit)] = 6
        elif not all(d in digit for d in d4):
            dmap[''.join(digit)] = 0
        else:
            dmap[''.join(digit)] = 9
    
    for digit in seg5:
        if all(d in digit for d in d1):
            dmap[''.join(digit)] = 3
        elif not all(d in d6 for d in digit):
            dmap[''.join(digit)] = 2
        else:
            dmap[''.join(digit)] = 5

    value = 0
    for digit in display:
        digit = ''.join(sorted(digit))
        value = value * 10 + dmap[digit]
    
    sum += value

print(sum)
