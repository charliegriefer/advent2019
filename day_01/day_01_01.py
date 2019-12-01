def main():
    with open("day_01.txt") as f:
        modules = [int(line) for line in f]
    print(sum([m//3 - 2 for m in modules]))


if __name__ == "__main__":
    main()
