def main():
    with open("day_02.txt") as f:
        intcode = list(map(int, f.read().split(",")))

    for noun in range(0, 99):
        for verb in range(0, 99):
            ic = [g for g in intcode]
            ic[1] = noun
            ic[2] = verb
            for g in [ic[i:i + 4] for i in range(0, len(ic), 4)]:
                if g[0] == 99:
                    break
                else:
                    ic[g[3]] = ic[g[1]] + ic[g[2]] if g[0] == 1 else ic[g[1]] * ic[g[2]]

                if ic[0] == 19690720:
                    print(100 * noun + verb)
                    break


if __name__ == "__main__":
    main()
