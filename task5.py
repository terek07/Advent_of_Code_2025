with open("input5.txt") as file:
    data = file.read()
data = data.split('\n\n')
fresh = [[int(e) for e in line.split('-')] for line in data[0].split('\n')]
ingredients = [int(e) for e in data[1].split('\n')]
# print(data)
# print(fresh)
# print(ingredients)
counter = 0
for ingredient in ingredients:
    for fresh_range in fresh:
        if fresh_range[1] + 1 >= ingredient >= fresh_range[0]:
            counter += 1
            break
print(counter)

# print(fresh)
fresh.sort()
# print(fresh)
norepeat_fresh = [fresh[0]]
for i, fresh_range in enumerate(fresh[1: ]):
    if fresh_range[0] <= norepeat_fresh[-1][1]:
        norepeat_fresh[-1] = ([min((fresh_range[0], norepeat_fresh[-1][0])), max((fresh_range[1], norepeat_fresh[-1][1]))])
        continue
    norepeat_fresh.append(fresh_range)

# print(norepeat_fresh)

counter2 = 0
for e in norepeat_fresh:
    counter2 += e[1] - e[0] + 1
print(counter2)
