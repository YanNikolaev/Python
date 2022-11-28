# f = open('1.txt', 'w')
# f.write('''Я к вам пишу — чего же боле?
# Что я могу еще сказать?
# Теперь, я знаю, в вашей воле
# Меня презреньем наказать.
# Но вы, к моей несчастной доле
# Хоть каплю жалости храня,
# Вы не оставите меня.
# Сначала я молчать хотела;
# Поверьте: моего стыда
# Вы не узнали б никогда,
# Когда б надежду я имела
# Хоть редко, хоть в неделю раз
# В деревне нашей видеть вас,
# Чтоб только слышать ваши речи,
# Вам слово молвить, и потом
# Все думать, думать об одном
# И день и ночь до новой встречи.
# Но, говорят, вы нелюдим;
# В глуши, в деревне всё вам скучно,
# А мы… ничем мы не блестим,
# Хоть вам и рады простодушно.''')
# f.close()
#

# f = open('1.txt', 'rt')
# print(f.read())
# f.close()

# # f = open('1.txt', 'rt')
# # for i in f:
# #     print(i)
# f.close()
# with open('1.txt', 'r') as f:
#     for i in f:
#         print(i)
# f.close()

# a = 'абвгдежзик'
# b = 'АБВГДЕЖЗИК'

# f = open('1.txt', 'r')
# text = f.read()
# f.close()

# new_text = ''
# for i in text:
#     for j in range(len(a)):
#         if i == a[j]:
#             i = b[j]
#     new_text += i
# print(new_text)
#
# f = open('newFile.txt', 'w')
# f.write(new_text)
# f.close()
#
# f = open('newFile.txt', 'r')
# print(f.read())
# f.close()

# f = open('1.txt', 'r')
# text = f.readlines()
# f.close()
#
# count = 0
# for i in text:
#     a = len(i.split())
#     count += a
#     print(count)
#
# count = (f"В тексте {count} слов.")
# f = open('1.txt', 'a')
# f.write(count)
# f.close()
#
# f = open('1.txt', 'r')
# print(f.read())
# f.close()


# f = open('1.txt', 'rt')
# print(f.read())
# f.close()

# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input('Введите число, на которое нужно сдвинуть текст: '))
#
# summary = ''
#
# def change(char):
#     if char in alpha:
#         return [(alpha.index(char) + number) % len(alpha)]
#     elif char in alphaUp:
#         return[(alphaUp.index(char) + number) % len(alphaUp)]
#     else:
#         return char
#
# with open('1.txt') as myfile:
#     for line in myfile:
#         for char in line:
#             summary += str(change(char))
#     #         print(f"Summary -- {summary}")
#     #     print(f"Char -- {char}")
#     # print(F'Line -- {line}')
# myfile.close()
#
# with open('output.txt', 'w', encoding="utf8") as myfile:
#     myfile.write(summary)
#
# with open('output.txt', 'r', encoding="utf8") as myfile:
#     print(myfile.read())
# myfile.close()

# a = open('filename2.txt', 'w')
# a.write('''Я помню чудное мгновенье:
# Передо мной явилась ты,
# Как мимолетное виденье,
# Как гений чистой красоты.
#
# В томленьях грусти безнадежной,
# В тревогах шумной суеты,
# Звучал мне долго голос нежный
# И снились милые черты.''')
# a.close()

# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input('Введите число, на которое нужно сдвинуть текст: '))
#
# summary = ''
#
#
# def changeChar(char):
#     if char in alpha:
#         return alpha[(alpha.index(char) + number) % len(alpha)]
#     elif char in alphaUp:
#         return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
#     else:
#         return char
#
#
# with open("filename2.txt", encoding="utf8") as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
#
# with open("output.txt", 'w', encoding="utf8") as myFile:
#     myFile.write(summary)
#
# with open('output.txt', 'r', encoding="utf8") as myfile:
#     print(myfile.read())
# myfile.close()

