import string

print("Давайте создадим пароль!")
print('Условия создания')
print("Длина пароля – 8 символов")
print("В пароле должны быть заглавные и строчные буквы, цифры и специальные символы")

password = input("Введите пароль: ")

a = any(symbol.isdigit() for symbol in password)

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
b = all(symbol in allowed for symbol in password)

g = any(char in "*- #" for char in password)


if len(password) < 8:
    print("Длина пароля не равна 8;")

elif password.lower() == password:
    print("В пароле отсутствуют заглавные буквы")

elif password.upper() == password:
    print("В пароле отсутствуют строчные буквы;")

elif a == False:
    print("В пароле отсутствуют цифры;")

elif b == False:
    print("В пароле используются непредусмотренные символы;")

elif g == False:
    print("В пароле отсутствуют специальные символы;")
else:
    print("Надёжный пароль!!!!!")
