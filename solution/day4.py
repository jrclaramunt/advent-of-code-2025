from utils.base import Day


class Day4(Day):
    def __init__(self, args):
        self.rolls_map = list(list())
        for row in range(len(args[0])):
            self.rolls_map.append(list(args[0][row].strip()))


    def part1(self):
        return self.access_rolls()

    def part2(self):
        total = 0
        rolls_accessed = -1

        while rolls_accessed != 0:
            rolls_accessed = self.access_rolls(update=True)
            total += rolls_accessed

        return total


    def access_rolls(self, update=False):
        total = 0
        for i in range(len(self.rolls_map)):
            for j in range(len(self.rolls_map[i])):
                adjacent_rolls = 0
                if self.rolls_map[i][j] == '@':
                    adjacent_rolls =\
                    self.verify_position(i, j + 1) +\
                    self.verify_position(i + 1, j + 1) +\
                    self.verify_position(i + 1, j) +\
                    self.verify_position(i + 1, j - 1) +\
                    self.verify_position(i, j - 1) +\
                    self.verify_position(i - 1, j - 1) +\
                    self.verify_position(i - 1, j) +\
                    self.verify_position(i - 1, j + 1)
                    if adjacent_rolls < 4:
                        total +=1
                        if update:
                            self.rolls_map[i][j] = '.'
                else:
                    continue
        return total


    def verify_position(self, i, j):
        if i < 0 or j < 0:
            return 0
        try:
            if self.rolls_map[i][j] == '@':
                return 1
            else:
                return 0
        except IndexError:
            return 0