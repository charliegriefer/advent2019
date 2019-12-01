def main():
    with open("day_01.txt") as f:
        modules = [int(line) for line in f]
    print(sum([recursive_fuel(m, 0) for m in modules]))


def recursive_fuel(m: int, result: int) -> int:
    fuel = m//3 - 2
    return result if fuel <= 0 else recursive_fuel(fuel, result + fuel)


if __name__ == "__main__":
    main()
