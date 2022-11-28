# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("-b-")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None

# for i, value in enumerate(list_):
#    if value < 0:
#        print("Отрицательное число: ", value)
#        index_negative = i  # перезаписываем значение индекса
#        print("Новый индекс отрицательного числа: ", index_negative)
#    else:
#        print("Положительное число: ", value)
#    print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
#
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """

# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
#
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
#
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

#
# while True:
#     if n % 3 == 0:
#          n = n // 3
#          if n == 1:
#               break
#     else:
#          break
# n = int(input("Введите число"))
#
# while True:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = (n * 3 + 1) // 2
#     print(n)
#
#     if n == 1:
#         print("Done")
# #         break
# N = 5
#
# for i in range(1, N + 1):
#    print("*" * i)
#
#  text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
#
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
#
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# text = input()  # получаем строку
#
# first = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
#
# for c in text:
#    if c == first:  # если символ совпадает с сохраненным,
#       count += 1  # то увеличиваем счетчик
#    else:
#       result += first + str(count)  # иначе - записываем в результат
#       first = c  # и обновляем сохраненный символ с его счетчиком
#       count = 1
#
# result += first + str(count)  # и добавляем в результат последний символ
# print(result)