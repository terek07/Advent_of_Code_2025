from operator import index

with open("input3.txt") as file:
    data = [e.strip() for e in file.readlines()]
print(data)
result = []
for e in data:
    id = -1
    x = 0
    for i in range(12, 0, -1):
        n = max(e[id + 1:-i])
        id = e.index(n)
        x += int(n) * (10 ** i)
    result.append(x)
print(result)
print(sum(result))

