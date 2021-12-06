import os

line_count = 0
bit_counts = []
with open("input.txt", "r", encoding='utf-8') as input:
    data = input.readlines()
    for line in data:
        line = line.strip()
        line_count += 1
        index = 0
        for letter in line:
            if (index + 1) > len(bit_counts):
                if letter == '1':
                    bit_counts.append(1)
                else:
                    bit_counts.append(0)
            else:
                if letter == '1':
                    bit_counts[index] += 1
            index += 1

epsilon_string = ''
gamma_string = ''

print('length is ' + str(line_count))
print(bit_counts)
for bit in bit_counts:
    if bit > line_count / 2:
        gamma_string += '1'
        epsilon_string += '0'
    else:
        gamma_string += '0'
        epsilon_string += '1'

epsilon_rate = int(epsilon_string, 2)
gamma_rate = int(gamma_string, 2)

print('epsilon: ' + str(epsilon_string))
print('epsilon: ' + str(epsilon_rate))
print('gamma: ' + str(gamma_string))
print('gamma: ' + str(gamma_rate))
print('power: ' + str(epsilon_rate * gamma_rate))
