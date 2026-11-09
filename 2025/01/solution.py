with open('input.txt') as data:
    part1 = 0
    part2 = 0
    dial = 50


    for row in data:
        change = int(row[1:])
        old_dial = dial

        if change >= 100:
            part2 += change // 100
            change %= 100

        if "L" in row:
            dial -= change
        if "R" in row:
            dial += change


        if old_dial != 0 and (dial <= 0 or dial >= 100):
            part2 += 1

        dial = dial % 100

        if dial == 0:
            part1 += 1


    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
