array = list(map(int, input("Введите последовательность чисел без повторяющихся значений через пробел:\t").split()))
set_array = set(array)
if len(array) != len(set_array):
    raise ValueError("Введены некорректные данные! Числа в последовательности не должны повторяться! ")
element = int(input("Введите любое число:\t"))
print(f"Отсортированный список: {sorted(array)}")
array.append(element)
array_sort = sorted(array)
print(f"Отсортированный список включающий введенное число: {array_sort}")

def binary_search(array_sort, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array_sort[middle] == element:
        return middle
    elif element < array_sort[middle]:
        return binary_search(array_sort, element, left, middle - 1)
    else:
        return binary_search(array_sort, element, middle + 1, right)


if array_sort[-1] <= element:
    print(f"Индекс меньшего элемента в последовательности, введенного вами числа:\n{len(array_sort) - 2}")
    print(f"Индекс введенного вами числа, если он будет в последовательности:\n{len(array_sort) - 1 }")
    print("Индекса большего элемента в последовательности, введенного вами числа, нет.")
elif array_sort[0] >= element:
    print("Индекса меньшего элемента в последовательности, введенного вами числа, нет.")
    print(f"Индекс введенного вами числа, если он будет в последовательности:\n{0}")
    print(f"Индекс большего элемента в последовательности, введенного вами числа:\n{1}")
else:
    print("Индекс меньшего элемента в последовательности, введенного вами числа:")
    print(binary_search(array_sort, element, 0, len(array_sort)) - 1)
    print(f"Индекс введенного вами числа, если он будет в последовательности:")
    print(binary_search(array_sort, element, 0, len(array_sort)))
    print("Индекс большего элемента в последовательности, введенного вами числа:")
    print(binary_search(array_sort, element, 0, len(array_sort)) + 1)
