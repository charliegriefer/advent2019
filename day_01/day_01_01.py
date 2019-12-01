def main():
    with open("day_01.txt") as f:
        modules = [int(line) for line in f]
    print(sum([x//3 - 2 for x in modules]))


if __name__ == "__main__":
    main()
