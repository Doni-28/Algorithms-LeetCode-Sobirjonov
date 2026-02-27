import random

def partition(arr, low, high):
    """
    Процедура разделения (partition) по схеме Ломуто.
    
    arr  — исходный массив
    low  — левая граница текущего подмассива
    high — правая граница текущего подмассива
    
    Возвращает индекс опорного элемента после разделения.
    """

    # В качестве pivot берём последний элемент (по схеме Ломуто)
    pivot = arr[high]

    # i — индекс "границы" элементов меньше pivot
    # все элементы <= pivot будут слева от i
    i = low - 1

    # Проход по массиву от low до high-1
    for j in range(low, high):
        # Если текущий элемент меньше или равен pivot
        if arr[j] <= pivot:
            i += 1
            # Меняем местами arr[i] и arr[j],
            # расширяя область элементов <= pivot
            arr[i], arr[j] = arr[j], arr[i]

    # После прохода ставим pivot на правильную позицию:
    # все элементы слева <= pivot, справа > pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Возвращаем индекс pivot
    return i + 1


def quick_sort(arr, low, high):
    """
    Быстрая сортировка (QuickSort) с рандомизированным выбором pivot.
    
    arr  — массив для сортировки (сортируется inplace)
    low  — левая граница
    high — правая граница
    """

    # Базовый случай рекурсии:
    # если в подмассиве 0 или 1 элемент — он уже отсортирован
    if low < high:

        # --- Рандоматизация ---
        # Выбираем случайный индекс в диапазоне [low, high]
        random_index = random.randint(low, high)

        # Меняем случайный элемент с последним,
        # чтобы использовать его как pivot по схеме Ломуто
        arr[random_index], arr[high] = arr[high], arr[random_index]

        # Разделяем массив относительно pivot
        pivot_index = partition(arr, low, high)

        # Рекурсивно сортируем левую часть (меньше pivot)
        quick_sort(arr, low, pivot_index - 1)

        # Рекурсивно сортируем правую часть (больше pivot)
        quick_sort(arr, pivot_index + 1, high)


# Пример использования

arr = [10, 7, 8, 9, 1, 5]
print("Исходный массив:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Отсортированный массив:", arr)