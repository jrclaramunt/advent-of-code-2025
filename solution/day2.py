import math
import re

from utils.base import Day


class Day2(Day):
    def __init__(self, args):
        self.ids_ranges = args[0][0].split(',')
        self.regex = r'(\d+)-(\d+)'

    def part1(self):
        total = 0
        for id_range in self.ids_ranges:
            id_range = re.match(self.regex, id_range).groups()
            total += self.get_invalid_ids(id_range)

        return total


    def part2(self):
        pass


    def get_invalid_ids(self, invalid_ids_range):
        first_id = invalid_ids_range[0]
        last_id = int(invalid_ids_range[1])

        total = 0
        cut = math.floor(len(first_id) / 2)

        base = str(first_id[0:cut])

        if base == '':
            base = '0'

        invalid_id = int(base + base)
        while invalid_id <= last_id:
            if invalid_id >= int(first_id):
                total += invalid_id

            base = str(int(base) + 1)
            invalid_id = int(base + base)

        return total
