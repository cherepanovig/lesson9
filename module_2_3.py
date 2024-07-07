my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] > 0:
       print(my_list[i])
    elif my_list[i] < 0:
        break
    i += 1
# Второй способ решения задачи
print('Выводим результат второго способа:')
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for item in my_list:
    if item > 0:
        print(item)
    elif item < 0:
        break

