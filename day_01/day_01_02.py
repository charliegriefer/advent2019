import math


def main():
    with open("day_01.txt") as f:
        modules = [line.rstrip("\n") for line in f]

    result = sum(map(lambda x: recursive_fuel(int(x), 0), modules))
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
