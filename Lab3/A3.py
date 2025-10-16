# Ввод данных
prev = int(input("Введите предыдущее показание счетчика: "))
curr = int(input("Введите текущее показание счетчика: "))

# Если счетчик "перевернулся" (прошел через 9999)
if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

print("Использовано газа:", used, "кубометров")

# Расчет стоимости
if used <= 300:
    cost = 21
elif used <= 600:
    cost = 21 + (used - 300) * 0.06
elif used <= 800:
    cost = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

# Средняя цена за 1 кубометр
price = cost / used if used > 0 else 0

# Округляем до 2 знаков
cost = round(cost, 2)
price = round(price, 2)

# Вывод результата
print("Сумма к оплате:", cost, "$")
print("Средняя цена за 1 кубометр:", price, "$")