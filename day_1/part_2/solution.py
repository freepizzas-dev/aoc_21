measurements = []
with open("input.txt", "r", encoding='utf-8') as input:
    input_lines = input.readlines()
    for line in input_lines:
        measurements.append(int(line))

index = 0
previous_window = None
increase_count = 0
while index < (len(measurements) - 2):
    window_total = measurements[index] + measurements[index + 1] + measurements[index + 2]
    if previous_window != None:
        if window_total > previous_window:
            increase_count += 1
    previous_window = window_total
    index += 1

print(increase_count)