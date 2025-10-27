a = input("Введите какую фигуру вы хотите нарисовать (P T R): ")
b= ['P','T','R']
for l in b:
    if a != b:
        break
    else:
        print('Введите корректную букву!')
n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))

if a == "P":
    for i in range(n):
        for j in range(m):
            print("&", end="")
        print()

elif a == "T":
    for i in range(1, n + 1):
        for j in range(i):
            print("&", end="")
        print()

elif a == "R":
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print("&", end="")
            else:
                print(" ", end="")
        print()