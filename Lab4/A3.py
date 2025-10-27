while True:
    s = input("Введите строку: ")
    if len(s) == 0:
        print("Строка не должна быть пустой")
        continue

    if len(s) <= 5:
        print("Строка должна превышать 5 символов!")
        continue

    if not all(c in "01" for c in s ):
        print("Строка должна содержать только 0 и 1. Попробуйте снова.")
        continue

    break

lose_summ = s.count("0")

max_zero = 0
current_zero = 0

for c in s:
    if c == "0":
        current_zero += 1
        if current_zero > max_zero:
            max_zero = current_zero
    else:
        current_zero = 0

prozent = (lose_summ / len(s)) * 100

print("Общее количество пакетов: ", len(s))
print("Количество потерянных пакетов: ", lose_summ)
print("Длина самой длинной последовательности потерянных пакетов: ", max_zero)
print(f"Процент потерь: {prozent:.1f}%")
if   0<= prozent < 1:
    print("Качество связи: Отличное качество!")
elif   1<= prozent <= 5:
    print("Качество связи: Хорошее качество")
elif  5< prozent <= 10:
    print("Качество связи: Удовлетворительное качество")
elif  10< prozent <= 20:
    print("Качество связи: Плохое качество")
elif prozent > 20:
    print("Качество связи: Критическое состояние сети")

