my_list_1 = [0, 1, 7, 2, 4, 8]
print("Вхідний список:", my_list_1)
my_list_2 = my_list_1[::2]

if not my_list_1:
    print("Список порожній")
else:
    print("Список з парними індексами:", my_list_2, "помножений на останій індекс", my_list_1[-1])
    print("Відповідь: ", sum(my_list_2 * my_list_1[-1]))