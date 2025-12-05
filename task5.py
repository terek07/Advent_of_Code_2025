from itertools import count

with open("input3.txt") as file:
    data = file.read()
data = data.split('\n\n')
fresh = [[int(e) for e in e.split('-')] for e in data[0].split('\n')]
ingredients = [int(e) for e in data[1].split('\n')]
# print(data)
# print(fresh)
# print(ingredients)

counter = 0
fresh.sort()
print(fresh)
norepeat_fresh = []
for i, fresh_range in enumerate(fresh[1: ]):
    if fresh_range[0] < fresh[i - 1][1]:
        norepeat_fresh.append([min((fresh_range[0], fresh[i - 1][0])), min((fresh_range[1], fresh[i - 1][1]))])
        #WIP
for ingredient in ingredients:
    for fresh_range in fresh:
        if fresh_range[1] + 1 >= ingredient >= fresh_range[0]:
            counter += 1
            break
print(counter)
# print(len(all_fresh))
