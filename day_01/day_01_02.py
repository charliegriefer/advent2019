import math
from itertools import repeat


def main():
    with open("day_01.txt") as f:
        modules = [int(line) for line in f]

    result = sum(map(recursive_fuel, modules, repeat(0)))
    print(result)


def recursive_fuel(n: int, s: int) -> int:
    fuel = calculate_fuel(n)

    if fuel <= 0:
        return s
    else:
        return recursive_fuel(fuel, s + fuel)


def calculate_fuel(n: int) -> int:
    return math.floor(n/3) - 2


if __name__ == "__main__":
    main()
