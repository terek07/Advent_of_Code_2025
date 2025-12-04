with open("input3.txt") as file:
    data = [e.strip() for e in file.readlines()]
print(data)
result = []
for e in data:
    id = -1
    x = 0
    for i in range(12, 0, -1):
        n = max(e[id + 1:len(e) - i + 1])
        id = e[id + 1:len(e) - i + 1].index(n) + id + 1
        print(n, id)
        x += int(n) * (10 ** (i - 1))
    result.append(x)
print(result)
print(sum(result))
