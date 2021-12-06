import os

#########################################################
#helper functions

#determine most common bit (tiebreaker = 1)
def generate_gamma(dataset):
    line_count = 0
    bit_counts = []
    for line in dataset:
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

    gamma_string = ''
    for bit in bit_counts:
        if bit >= line_count / 2:
            gamma_string += '1'
        else:
            gamma_string += '0'
    return gamma_string

#determine least common bit (tiebreaker = 0)
def generate_epsilon(dataset):
    line_count = 0
    bit_counts = []
    for line in dataset:
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
    for bit in bit_counts:
        if bit < line_count / 2:
            epsilon_string += '1'
        else:
            epsilon_string += '0'
    return epsilon_string

#####################################################

oxygen_data = []
co2_data = []
with open("input.txt", "r", encoding='utf-8') as input:
    data = input.readlines()
    epsilon_string = generate_epsilon(data)
    gamma_string = generate_gamma(data)
    for line in data:
        line = line.strip() #strip newline character at end of each line
        oxygen_data.append(line)
        co2_data.append(line)

index = 0
while (len(oxygen_data) > 1) and (index < len(gamma_string)):
    oxygen_data[:] = [item for item in oxygen_data if item[index] == gamma_string[index]] #might need to add a len(oxygen_data) > 1 check here?
    gamma_string = generate_gamma(oxygen_data)
    index += 1
print('found oxygen candidate ' + str(oxygen_data) + "\n")

index = 0
while (len(co2_data) > 1) and (index < len(epsilon_string)):
    co2_data[:] = [item for item in co2_data if item[index] == epsilon_string[index]] #same as above
    epsilon_string = generate_epsilon(co2_data)
    index += 1
print('found co2 candidate ' + str(co2_data) + "\n")

oxygen_rating = int(oxygen_data[0], 2)
co2_rating = int(co2_data[0], 2)
lifesupport_rating = oxygen_rating * co2_rating
print('oxygen: ' + str(oxygen_rating))
print('co2: ' + str(co2_rating))
print('lifesupport: ' + str(lifesupport_rating))
