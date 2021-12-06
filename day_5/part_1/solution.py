#first we should determine the size of the grid we're working with
max_x = 0
max_y = 0
with open("input.txt", "r", encoding='utf-8') as input:
    data = input.readlines()
    for line in data:
        coords = line.split(' -> ')
        for pair in coords:
            x = int(pair.split(',')[0])
            y = int(pair.split(',')[1])
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

#generate empty 2d grid of required size
grid = []
while len(grid) <= max_x:
    temp_x = []
    while len(temp_x) <= max_y:
        temp_x.append(0)
    grid.append(temp_x)

#read lines and mark how many times each grid point is touched
with open("input.txt", "r", encoding='utf-8') as input:
    data = input.readlines()
    for line in data:
        coords = line.strip().split(' -> ')
        x1 = int(coords[0].split(',')[0])
        x2 = int(coords[1].split(',')[0])
        y1 = int(coords[0].split(',')[1])
        y2 = int(coords[1].split(',')[1])
        
        #consider non-diagonal lines only
        if (x1 == x2) or (y1 == y2):
            #check for horizontal line
            if (x1 != x2):
                if (x1 < x2):
                    while(x1 <= x2):
                        grid[x1][y1] += 1
                        x1 += 1
                elif (x1 > x2):
                    while (x1 >= x2):
                        grid[x1][y1] += 1
                        x1 -= 1

            #check for vertical line
            if (y1 != y2):
                if (y1 < y2):
                    while(y1 <= y2):
                        grid[x1][y1] += 1
                        y1 += 1
                elif (y1 > y2):
                    while (y1 >= y2):
                        grid[x1][y1] += 1
                        y1 -= 1

danger = 0
for x in grid:
    for value in x:
        if value > 1:
            danger += 1

print('danger zones: ' + str(danger))