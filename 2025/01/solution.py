with open('input.txt') as data:
    part1 = 0
    part2 = 0
    dial = 50

    for row in data:
        for i in range(int(row[1:])):
            if row[0] == "R":
                dial += 1
                if dial > 99:
                    dial = 0
                if dial == 0 and (i + 1) == int(row[1:]):
                    part1 += 1
                if dial == 0:
                    part2 += 1

            else:
                dial -= 1
                if dial < 0:
                    dial = 99
                if dial == 0 and (i + 1) == int(row[1:]):
                    part1 += 1
                if dial == 0:
                    part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
