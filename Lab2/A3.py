import sys
from sys import getsizeof

byte_size = 1921000

# Считаем кол-во мегабайт

megabyte = byte_size / (1024 * 1024)


# Выводим кол-во мегабайт и проверяем результат функицей гетсайз
print(megabyte)
print(getsizeof(megabyte))