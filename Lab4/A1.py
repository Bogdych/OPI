import random
import time

correct_otv = 0         # количество правильных ответов
o_time = 0      # общее время

N = int(input("Введите кол-во примеров: "))
for i in range(N):
    a: int = random.randint(2, 9)
    b: int = random.randint(2, 9)

    while True:   #бесконечный цикл
        try:
            start_time = time.time()   #текущее время
            answer = int(input(f"{i+1}) {a} * {b} = "))   #ввод пользователя
            time_s = time.time() - start_time

            # Проверяем правильность ответа
            if answer == a * b:
                print(f"Верно! (Время: {time_s:.2f} сек)\n")
                correct_otv += 1
            else:
                print(f"Неверно! Правильный ответ: {a * b}. (Время: {time_s:.2f} сек)\n")

            break   #выходим из цикла, если ввод OK
        except ValueError:   #отлавливаем ошибку ввода
            print("Пожалуйста, введите целое число!")

    o_time += time_s
s_time = o_time / N
proz_otv = (correct_otv / N) * 100

print("==================================================\n СТАТИСТИКА: =================================================\n")
print(f"Общее время, затраченное на ответы: {o_time:.1f}сек")
print(f"Среднее время на один пример: {s_time:.1f}сек")
print("Количество правильных ответов: ",correct_otv,"/",N)
print(f"Процент правильных ответов:  {proz_otv:.1f}%")