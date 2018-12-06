# Challenge 1
# Frequency addition

input_file = "input.txt"
starting_val = 0

with open(input_file, "r") as f:
    for line in f.read().split('\n'):
        if len(line) < 2:
            pass
        elif line[0] == '+':
            starting_val += int(line[1:])
        elif line[0] == '-':
            starting_val -= int(line[1:])
print(starting_val)
