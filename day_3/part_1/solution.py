#count the number of '1's in each bit; if it's greater than half the length,
#it's the 'most common bit' for that position
line_count = 0
bit_counts = []
with open("input.txt", "r", encoding='utf-8') as input:
    data = input.readlines()
    for line in data:
        line = line.strip() #strip newline character at end of each line
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
power = epsilon_rate * gamma_rate

print('epsilon(2): ' + str(epsilon_string))
print('gamma(2): ' + str(gamma_string))
print('epsilon(10): ' + str(epsilon_rate))
print('gamma(10): ' + str(gamma_rate))
print('power: ' + str(power))
