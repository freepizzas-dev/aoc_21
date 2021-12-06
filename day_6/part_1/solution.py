school = []
days_to_run = 80
days_passed = 0

#get fish initial state
with open("input.txt", "r", encoding='utf-8') as input:
    data = input.readlines()
    for line in data:
        school = line.split(',')

while days_passed < days_to_run:
    temp_school = []
    for fish in school:
        if int(fish) == 0:
            temp_school.append(6)
            temp_school.append(8)
        else:
            temp_school.append(int(fish) - 1)
    school = temp_school
    days_passed += 1

print(len(school))