from utils.base import Day


class Day3(Day):
    def __init__(self, args):
        input_banks = list(map(lambda x: list(x.strip()), args[0]))

        self.banks = []
        for input_bank in input_banks:
            self.banks.append(list(map(lambda x: int(x), input_bank)))


    def part1(self):
        total = 0
        for bank in self.banks:
            first_digit = max(bank)

            index = bank.index(first_digit)
            if index == len(bank) - 1:
                second_digit = first_digit
                first_digit = max(bank[0:index])
            else:

                second_digit = max(bank[index + 1:])
            total += first_digit * 10 + second_digit

        return total


    def part2(self):
        total = 0
        total_batteries = 12

        for bank in self.banks:
            lower_limit = 0
            upper_limit = len(bank)
            remaining_batteries = total_batteries
            max_joltage = ''

            while remaining_batteries > 0:
                digit = max(bank[lower_limit:upper_limit])
                index = bank.index(digit)

                if index > len(bank) - (total_batteries - len(max_joltage)):
                    upper_limit = index
                else:
                    for _ in range(index + 1):
                        bank.pop(0)

                    upper_limit = len(bank)
                    max_joltage += str(digit)
                    remaining_batteries -= 1

            total += int(max_joltage)

        return total
