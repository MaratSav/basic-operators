my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
    if index >= len(my_list):
        break
    my_int = my_list[index]
    if my_int >= 0:
        continue
    else:
        break