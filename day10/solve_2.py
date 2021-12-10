with open('input', 'r') as input_file:
    data = input_file.readlines()

mapping = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []
for line in data:
    stack = []
    for c in line.strip():
        if c in mapping:
            stack.append(c)
        elif c != mapping[stack.pop()]:
            break
    else:
        score = 0
        for c in stack[::-1]:
            score = score * 5 + points[mapping[c]]
        scores.append(score)

scores = sorted(scores)
print(scores[len(scores) // 2])
