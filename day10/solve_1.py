with open('input', 'r') as input_file:
    data = input_file.readlines()

mapping = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in data:
    stack = []
    for c in line.strip():
        if c in mapping:
            stack.append(c)
        elif c != mapping[stack.pop()]:
            score += points[c]

print(score)
