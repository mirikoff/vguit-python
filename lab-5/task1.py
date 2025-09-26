# Дана строка, содержащая русскоязычный текст. Найти количество слов,
# начинающихся с буквы "е".

str = str(input('Введите строку: '))
str.split()

i = 0

for char in str:
    if char.lower().startswith("е"):
        i = i + 1
    else: continue


print('Количество "е" в строчке: ', i)