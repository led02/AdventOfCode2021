with open('input', 'r') as input_file:
    data = list(map(int, input_file.readlines()))

increase = sum(map(lambda x: x[1] > x[0], zip(data[:-1], data[1:])))
print(increase)
