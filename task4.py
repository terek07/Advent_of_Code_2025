with open("input4.txt") as file:
    data = [e.strip() for e in file.readlines()]
print(data)

result = 0
for x, row in enumerate(data):
    for y, e in enumerate(row):
        if e != "@":
            continue
        counter = 0
        for px in range(-1, 2):
            if x + px >= len(data) or x + px < 0:
                continue
            for py in range(-1, 2):
                if y + py >= len(row) or y + py < 0:
                    continue
                if data[x + px][y + py] == "@":
                   counter += 1
        if counter < 5:
            result += 1
print(result)

