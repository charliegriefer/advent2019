import math


def main():
    with open("day_01.txt") as f:
        modules = [line.rstrip("\n") for line in f]
    result = sum(map(lambda x: math.floor(int(x)/3) - 2, modules))

    print(result)


if __name__ == "__main__":
    main()
