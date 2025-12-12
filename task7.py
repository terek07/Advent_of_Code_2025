with open("input7.txt") as file:
    data = file.readlines()
# part1
result = 0
for y in range(len(data)):
    for x in range(1, len(data[0]) - 1):
        if data[y][x] == '^':
            for i in range(1, y):
                if data[y - i][x - 1] == '^' or data[y - i][x + 1] == '^':
                    result += 1
                    break
                if data[y - i][x] == '^':
                    break
print(result + 1)

