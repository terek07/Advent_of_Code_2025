with open("input1.txt") as file:
    data = file.readlines()
current_place = 50
zero_counter = 0
for e in data:
    direction_is_right = e[0] == 'R'
    if direction_is_right:
        current_place += int(e[1:-1])
        while current_place > 100:
            zero_counter += 1
            current_place -= 100
        current_place %= 100
    else:
        current_place -= int(e[1:-1])
        while current_place < 0:
            if current_place + int(e[1:-1]) == 0:
                zero_counter -= 1
            zero_counter += 1
            current_place += 100
        current_place %= 100
    if current_place == 0:
        zero_counter += 1
    print(current_place)
print(zero_counter)
