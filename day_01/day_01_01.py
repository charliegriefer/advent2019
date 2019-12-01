import math


def main():
    with open("day_01.txt") as f:
        modules = [int(line) for line in f]
    result = sum([math.floor(x/3) - 2 for x in modules])
    print(result)


if __name__ == "__main__":
    main()
