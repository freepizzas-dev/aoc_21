import os

with open("input.txt", "r", encoding='utf-8') as input:
    input_lines = input.readlines()
    previous_number = None
    increase_count = 0
    for line in input_lines:
        if previous_number != None:
            if int(line) > previous_number:
                increase_count += 1
        previous_number = int(line)

print(increase_count)