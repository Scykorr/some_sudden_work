"""
Функция создания матрицы на вход подается число строк и столбцов
"""


def create_matrix(rows, columns) -> list:
    # создаем пустой список
    result_matrix = []
    # цикл по количеству строк
    for row_num in range(rows):
        print(f'Строка {row_num}')
        # генерация строки списка по количеству столюцов
        new_row = [int(input(f'Введите значение в строке под номером {column_num}: ')) for column_num in
                   range(columns)]
        result_matrix.append(new_row)
    # возвращаем полученную матрицу
    return result_matrix


"""
Функция вывода матрицы, на вход подается соответствующая матрица
"""


def print_matrix(matrix) -> None:
    print('\nИтоговая матрица:', *matrix, sep='\n')


"""
Функция нахождения максимального отрицательного элемента и минимального положительного,
с последующей заменой строк по индексам, где эти элементы находятся
"""


def replace_row(matrix) -> None:
    # задаем начальные значения индексов и минимального и максимального значения
    max_num = 0
    max_index = 0
    min_num = -1
    min_index = 0
    # цикл по строкам матрица
    for index, row in enumerate(matrix):
        # вложенный цикл по элементам строки
        for el in row:
            # если максимальное отрицательное число больше элемента
            # или найдено первое отрицательно число при начальном значении max_num,
            # присваиваем индексу и max_num текущие значения
            if max_num < el < 0 or max_num == 0 and el < 0:
                max_num = el
                max_index = index
            # если минимальное положительное число меньше элемента
            # или найдено первое положительное число при начальном значении min_num,
            # присваиваем индексу и mix_num текущие значения
            if min_num > el > 0 or min_num == -1 and el > 0:
                min_index = index
                min_num = el
    # переставляем строки матрицы в соответствии с найденными индексами
    matrix[max_index], matrix[min_index] = matrix[min_index], matrix[max_index]


if __name__ == '__main__':
    inp_row = int(input('Введите количество строк: '))
    inp_column = int(input('Введите количество столбцов: '))
    first_matrix = create_matrix(rows=inp_row, columns=inp_column)
    print_matrix(first_matrix)
    replace_row(first_matrix)
    print_matrix(first_matrix)
