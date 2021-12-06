fish_pop = [0] * 9
with open('input', 'r') as input_file:
    for ctr in map(int, input_file.readline().split(',')):
        fish_pop[ctr] += 1

for _ in range(256):
    print(fish_pop)
    fish_pop[7] += fish_pop[0]
    fish_pop = fish_pop[1:] + fish_pop[:1]

print(sum(fish_pop))
