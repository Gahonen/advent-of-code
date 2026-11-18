with open('input.txt') as data:
    part1 = []
    part2 = []
    first_id = 0
    last_id = 0
    id_ranges = data.read().split(",")

    # Length of longest ID
    len_long = int((len(str(max(id_ranges, key=len))) - 1))

    for ranges in range(len(id_ranges)):
        # Setting value before "-" as the first value of current ID range
        first_id = int(id_ranges[ranges].split("-")[0])
        # Setting value after "-" as the last value of current ID range
        last_id = int(id_ranges[ranges].split("-")[1])
        current_id = first_id

        # Looping through all the ID's
        for ids in range(last_id - (first_id - 1)):
            # Getting the length of the current ID
            len_id = len(str(current_id))

            # For each part in a quarter of an ID
            for part in range(int(len_long / 4) + 1):
                # Part is counting the parts the ID can be divided into
                # Part will be at least 2 since ID divided by itself would always be invalid
                part += 2
                # If the lenght of the ID is divisible by the part
                # Essentially checks if the ID can be divided equal parts
                if len_id % part == 0:

                    # Checks if part is equal to the amount of times the first
                    # x numbers of current ID
                    if part == str(current_id).count(str(current_id)[:int(len_id / part)]):
                        if part == 2 and current_id not in part1:
                            part1.append(current_id)
                        if current_id not in part2:
                            part2.append(current_id)

            current_id += 1

    print(f"Part 1: {sum(part1)}")
    print(f"Part 2: {sum(part2)}")
