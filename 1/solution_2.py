# Challenge 2
# Day 1

input_file = "input.txt"
starting_val = 0
val_set = set([0])
i = 0

with open(input_file, "r") as f:
    val_list = [x for x in f.read().split('\n') if len(x) >= 2]
    while 1:
        line = val_list[i % len(val_list)]
        i += 1
        if line[0] == '+':
            starting_val += int(line[1:])
        elif line[0] == '-':
            starting_val -= int(line[1:])
        if starting_val in val_set:
            print(starting_val)
            break
        else:
            val_set.add(starting_val)
