# В комментарий записаны те числа которые нельзя перевести

#a = int('123е') Не получается приобразовать в дес. число. Ошибка: ValueError: invalid literal for int() with base 10: '123е'
#b = int('91.4') Не получается приобразовать в дес. число. Ошибка: ValueError: invalid literal for int() with base 10: '91.4'
#c = int(524.345 ** 435345345311145345) Не получается приобразовать в дес. число. Ошибка: OverflowError: (34, 'Result too large')
#d = int('7.1 + 4') Не получается приобразовать в дес. число. Ошибка: ValueError: invalid literal for int() with base 10: '7.1 + 4'
#g = int('4' - 2) Не получается приобразовать в дес. число. Ошибка: TypeError: unsupported operand type(s) for -: 'str' and 'int'
#z = int('4 - 2') Не получается приобразовать в дес. число. Ошибка: ValueError: invalid literal for int() with base 10: '4 - 2'
x = int('42')
y = int(-12.12)

#Выводим те числа, которые можно перевести в дес. число
print(x)
print(y)
print ("x и y можно преобразовать в дес. число!")