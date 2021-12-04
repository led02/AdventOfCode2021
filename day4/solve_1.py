class BingoBoard:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def draw(self, number):
        for row in self.numbers:
            for col, num in enumerate(row):
                if num == number:
                    row[col] = -num - 1
                    break
            else:
                continue
            break
    
    def check(self):
        for row in self.numbers:
            if all(map(lambda x: x < 0, row)):
                return True
        
        for col in zip(*self.numbers):
            if all(map(lambda x: x < 0, col)):
                return True
        
        return False
    
    def score(self, draw):
        bsum = 0
        for row in self.numbers:
            for num in row:
                if num >= 0:
                    bsum += num
        return bsum * draw

with open('input', 'r') as input_file:
    draws = map(int, input_file.readline().split(','))
    boards_data = input_file.read().strip().split('\n\n')

boards = []
for board_data in boards_data:
    rows = board_data.split('\n')
    numbers = []
    for row in rows:
        numbers.append([int(row[3 * n:3 * n + 2]) for n in range(5)])
    boards.append(BingoBoard(numbers))

for number in draws:
    for board in boards:
        board.draw(number)
        if board.check():
            print(board.score(number))
            break
    else:
        continue
    break

