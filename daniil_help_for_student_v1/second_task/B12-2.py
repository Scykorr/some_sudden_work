from operator import itemgetter
from time import time

"""
Функция формирования списка(массива)
list() - функция, задающая список для переменной inp_list
map() - функция, применяющая функцию(первый аргумент) float(преобразует переданную строку в число вещественного типа)
        к введенному списку значений(второй аргумент)
данная функция возвращает список введенных в строку вещественных значений
"""


def form_list() -> list:
    inp_list = list(map(float, input('Введите элементы массива через пробел: ').split()))
    return inp_list


"""
Функция вывода исходного массива по k-ый элемент(элементы считаются с 0)
inp_num_k - ввод числа k
далее идет проверка входит ли введенное число в промежуток значений индексов элементов массива
если входит, построчно выводит элементы до k-ого включительно
если не входит, уведомляет пользователя о невозможности выполнить вывод
"""


def print_list(res_list) -> None:
    inp_num_k = int(input('По какой элемент массива осуществлять вывод?\n'
                          '(нумерация элементов начинается с 0): '))
    if 0 <= inp_num_k <= (len(res_list) - 1):
        for index in range(inp_num_k + 1):
            print(res_list[index])
    else:
        print('Введенное Вами число не является индексом из данного массива!')


"""
Функция, описывающая сортировку методом "пузырька"
len_list - переменная, содержащая длину списка для сортировки
В сортировке методом пузырька количество итераций внешнего цикла определяется длинной списка минус единица,
так как когда второй элемент становится на свое место, то первый уже однозначно минимальный и не требует сортировки.
Количество итераций внутреннего цикла зависит от номера итерации внешнего цикла, так как конец списка уже отсортирован,
и выполнять проход по этим элементам смысла нет.
"""


def bubble_sort(inp_list):
    len_list = len(inp_list)
    for i in range(len_list - 1):
        for j in range(len_list - 1 - i):
            if inp_list[j] > inp_list[j + 1]:
                inp_list[j], inp_list[j + 1] = inp_list[j + 1], inp_list[j]


"""
Предполагается, что первый элемент списка отсортирован. 
Переходим к следующему элементу, обозначим его х. 
Если х больше первого, оставляем его на своём месте. 
Если он меньше, копируем его на вторую позицию, а х устанавливаем как первый элемент.

Переходя к другим элементам несортированного сегмента, 
перемещаем более крупные элементы в отсортированном сегменте вверх по списку,
пока не встретим элемент меньше x или не дойдём до конца списка.
В первом случае x помещается на правильную позицию.
"""


def index_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert


# Функция сравнения скорости выполнения алгоритмов
def check_speed(bubble_speed, index_speed):
    if bubble_speed < index_speed:
        print('Метод "Пузырьком" быстрее')
    elif bubble_speed == index_speed:
        print('Методы работы имеют одинаковую скорость')
    else:
        print('Метод "индексами" быстрее')


"""
Функция сдвига на вход получает список и шаг сдвига, далее в цикле по количеству шагов происходит
удаление элемента с конца списка и вставка его в начало списка
"""


def shift_func(inp_list, step):
    for _ in range(step):
        inp_list.insert(0, inp_list.pop(-1))
    print(inp_list)


if __name__ == '__main__':
    # часть 1

    # ввод элементов
    part_1_list = form_list()
    # вывод элементов по k-ый элемент
    print_list(part_1_list)

    # часть 2

    # ввод двух массивов вещественных чисел
    inp_first_list_bubble_sort = form_list()
    inp_second_list_bubble_sort = form_list()
    # создание копий массивов для сортировки "индексами"
    inp_first_list_index_sort = inp_first_list_bubble_sort.copy()
    inp_second_list_index_sort = inp_second_list_bubble_sort.copy()

    # пузырьком
    # счетчик начала выполнения функции
    start_time_first = time()
    # выполнение функции сортировки
    bubble_sort(inp_first_list_bubble_sort)
    # счетчик конца выполнения функции
    first_list_bubble_sort_time = time() - start_time_first
    # вывод времени выполнения первой сортировки и отсортированного массива
    print("Время выполнения сортировки первого массива методом 'Пузырька':", first_list_bubble_sort_time)
    print("Результат сортировки:", inp_first_list_bubble_sort)

    # счетчик начала выполнения функции
    start_time_second = time()
    # выполнение функции сортировки
    bubble_sort(inp_second_list_bubble_sort)
    # счетчик конца выполнения функции
    second_list_bubble_sort_time = time() - start_time_second
    # вывод времени выполнения второй сортировки и отсортированного массива
    print("Время выполнения сортировки второго массива методом 'Пузырька':", second_list_bubble_sort_time)
    print("Результат сортировки:", inp_second_list_bubble_sort)

    # индексами
    # счетчик начала выполнения функции
    start_time_first = time()
    # выполнение функции сортировки
    index_sort(inp_first_list_bubble_sort)
    # счетчик конца выполнения функции
    first_list_index_sort_time = time() - start_time_first
    # вывод времени выполнения первой сортировки и отсортированного массива
    print("Время выполнения сортировки первого массива индексами:", first_list_index_sort_time)
    print("Результат сортировки:", inp_first_list_index_sort)

    # счетчик начала выполнения функции
    start_time_second = time()
    # выполнение функции сортировки
    index_sort(inp_second_list_bubble_sort)
    # счетчик конца выполнения функции
    second_list_index_sort_time = time() - start_time_second
    # вывод времени выполнения второй сортировки и отсортированного массива
    print("Время выполнения сортировки второго массива индексами:", second_list_index_sort_time)
    print("Результат сортировки:", inp_second_list_index_sort)

    print('Для первого массива:', end=' ')
    check_speed(first_list_bubble_sort_time, first_list_index_sort_time)
    print('Для второго массива:', end=' ')
    check_speed(second_list_bubble_sort_time, second_list_index_sort_time)

    # Функция сдвига массива из части 1
    print('Массив из первой части после сдвига:')
    shift_func(inp_list=part_1_list, step=3)
