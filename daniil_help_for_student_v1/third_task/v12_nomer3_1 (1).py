import numpy as np


def practica(q, e, a):
    # Инициализация переменных
    z = 0
    x = 0
    j = 0

    # Поиск первой отрицательной переменной
    for i in range(q):
        for k in range(e):
            if a[i, k] < 0:
                j = i
                x = k
                break
        if a[i, k] < 0:
            break

    # Поиск наименьшего положительного элемента в массиве
    for i in range(q):
        for k in range(e):
            if a[i, k] < a[z, x] and a[i, k] > 0:
                z = i
                x = k

    x = 0
    # Поиск элемента с наименьшим по модулю отрицательным значением
    for i in range(q):
        for k in range(e):
            if abs(a[i, k]) < abs(a[j, x]) and a[i, k] < 0:
                j = i
                x = k

    # Обмен строк, содержащих найденные элементы
    s = np.copy(a[z, :])
    a[z, :] = a[j, :]
    a[j, :] = s


# Основная программа
def main():
    # Ввод количества строк
    r = int(input("Введите количество строк: "))

    # Ввод количества столбцов
    t = int(input("Введите количество столбцов: "))

    # Создание массива
    o = np.zeros((r, t))

    # Ввод элементов массива
    print("Введите массив")
    for i in range(r):
        o[i, :] = list(map(float, input().split()))

    print("Исходный массив:")
    # Вывод исходного массива
    for i in range(r):
        print(o[i, :])

    # Вызов подпрограммы для обработки массива
    practica(r, t, o)

    print("Изменённый массив:")
    # Вывод измененного массива
    for i in range(r):
        print(o[i, :])
        


if __name__ == "__main__":
    main()
