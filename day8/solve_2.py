with open('input', 'r') as input_file:
    data = [
        (head.strip().split(' '), tail.strip().split(' '))
        for head, tail in map(lambda s: s.split(' | '), input_file.readlines())
    ]

sum = 0
for detect, display in data:
    seg5 = []
    seg6 = []
    dmap = {}
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
        if d1[0] not in digit or d1[1] not in digit:
            d6 = digit
            dmap[''.join(digit)] = 6
        elif d4[0] not in digit or d4[1] not in digit or d4[2] not in digit or d4[3] not in digit:
            dmap[''.join(digit)] = 0
        else:
            dmap[''.join(digit)] = 9
    
    for digit in seg5:
        if d1[0] in digit and d1[1] in digit:
            dmap[''.join(digit)] = 3
        elif digit[0] not in d6 or digit[1] not in d6 or digit[2] not in d6 or digit[3] not in d6 or digit[4] not in d6:
            dmap[''.join(digit)] = 2
        else:
            dmap[''.join(digit)] = 5

    value = 0
    for digit in display:
        digit = ''.join(sorted(digit))
        value = value * 10 + dmap[digit]
    
    sum += value

print(sum)
