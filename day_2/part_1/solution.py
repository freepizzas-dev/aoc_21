import os

depth = 0
horiz_pos = 0
with open("input.txt", "r", encoding='utf-8') as input:
    instructions = input.readlines()
    for line in instructions:
        data = line.split(" ")
        if data[0] == "forward":
            horiz_pos += int(data[1])
        if data[0] == "down":
            depth += int(data[1])
        if data[0] == "up":
            depth -= int(data[1])

print('final depth: ' + str(depth))
print('final horiz_pos: ' + str(horiz_pos))
print('product: ' + str(depth * horiz_pos))