def main():
    with open("day_02.txt") as f:
        intcode = list(map(int, f.read().split(",")))

    intcode[1] = 12
    intcode[2] = 2

    for g in [intcode[i:i + 4] for i in range(0, len(intcode), 4)]:
        if g[0] == 99:
            break
        else:
            intcode[g[3]] = intcode[g[1]] + intcode[g[2]] if g[0] == 1 else intcode[g[1]] * intcode[g[2]]

    print(intcode[0])


if __name__ == "__main__":
    main()
