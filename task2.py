with open("input2.txt") as file:
    data = [(int(e.split("-")[0]), int(e.split("-")[1])) for e in file.read().split(",")]
# print(data)
#task1
# result = 0
# for e in data:
#     for i in range(e[0], e[1] + 1):
#         x = str(i)
#         split_point = len(x) // 2
#         a = x[:split_point]
#         b = x[split_point:]
#         if a==b:
#             result += i
#         # print(a, b)
# print(result)

result = 0

for start, end in data:
    for i in range(start, end + 1):
        s = str(i)
        length = len(s)

        for n in range(2, length + 1):
            if length % n != 0:
                continue
                
            part_len = length // n
            part = s[:part_len]

            if part * n == s:
                result += i
                break

print(result)



