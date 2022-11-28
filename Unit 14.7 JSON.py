import json


# with open('json_example.json', encoding='utf8') as f:
#     templates = json.load(f)
#
# print(templates)
# print(type(templates))
#
#
#
# with open('json_example.json', encoding='utf8') as f:
#     strfile = f.read()
#     templates = json.loads(strfile)
#
# print(templates)
# print(type(templates))








# template = {
#     'firstname': 'Иван',
#     'lastname': 'Иванов',
#     'isAlive': True,
#     'age': 32,
#     'address': {
#         'streetAddress': 'Нейбута 32',
#         'city': 'Владивосток',
#         'state': '',
#         'postalcode': ''
#     },
#     'phoneNumbers': [
#         {
#             'type': 'mob',
#             'number': '123-333-4455'
#         },
#         {
#             'type': 'office',
#             'number': '123 111-4567'
#         }
#     ],
#     'children': [],
#     'spouse': None
# }
#
# with open('to_json_example.json', 'w', encoding='utf8') as f:
#     json.dump(template, f, ensure_ascii=False, indent=4)
#
# with open('to_json_example.json', encoding='utf8') as f:
#     print(f.read())
#
#
# def changeText(text):
#     """
#     Функция принимает строку с текстом.
#     Убирает все знаки препинания и возвращает
#     список, состоящий из слов текста.
#     """
#
#
#     for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#         text = text.replace(i, '')
#
#     return text.split()
#
#
# def mostCommon(text, length=0):
#     """
#     Функция принимает список и ограничение по длине.
#     Возвращает самый часто встречающийся элемент.
#     Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
#     """
#
#
#     most_common = []
#     qty_most_common = 0
#
#     for item in text:
#         if len(item) > length:
#             qty = text.count(item)
#             if qty > qty_most_common and qty > 2:
#                 qty_most_common = qty
#                 most_common = [item]
#             elif qty == qty_most_common:
#                 most_common.append(item)
#
#     return list(set(most_common))
#
#
# def mostLength(text):
#     """
#     Функция принимает список.
#     Возвращает самый длинный элемент.
#     Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
#     """
#
#
#     most_length = []
#     qty_most_length = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for item in text:
#         for char in item:
#             if char not in alphabet:
#                 charEn = False
#             else:
#                 charEn = True
#
#     if charEn:
#         qty = len(item)
#         if qty > qty_most_length:
#             qty_most_length = qty
#             most_length = [item]
#         elif qty == qty_most_length:
#             most_length.append(item)
#
#     return list(set(most_length))
#
# nameFile = input('Название файла: ')
#
# with open(nameFile, encoding='utf8') as f:
#     fileText = f.read()
#
# fileText = changeText(fileText)
# print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLength(fileText)}')