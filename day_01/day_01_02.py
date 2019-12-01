def main():
    with open("day_01.txt") as f:
        modules = [int(line) for line in f]
    print(sum([recursive_fuel(x, 0) for x in modules]))


def recursive_fuel(n: int, s: int) -> int:
    fuel = n//3 - 2
    return s if fuel <= 0 else recursive_fuel(fuel, s + fuel)


if __name__ == "__main__":
    main()
