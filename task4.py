with open("input3.txt") as file:
    data = [list(e.strip()) for e in file.readlines()]
print(data)

results = []

def remove_avaible(data=data):
    result = 0
    removed = False
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
                data[x][y] = '.'
                removed = True
    print(result)
    results.append(result)
    return removed
while remove_avaible():
    remove_avaible()
print(sum(results))
