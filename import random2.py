import random

def partition(arr, low, high):
    """
    Функция partition по схеме Lomuto.
    Делит массив на элементы меньше или равные pivot и больше pivot.
    Возвращает индекс pivot после разбиения.
    """
    pivot = arr[high]  # Опорный элемент
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Ставим pivot на правильное место
    return i + 1

def quick_select(arr, k):
    """
    QuickSelect для поиска k-го наименьшего элемента.
    k начинается с 0.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Случайный выбор опорного элемента для рандомизации
        rand_index = random.randint(low, high)
        arr[rand_index], arr[high] = arr[high], arr[rand_index]

        # Разделение массива
        pi = partition(arr, low, high)

        if pi == k:
            # Нашли k-й наименьший элемент
            return arr[pi]
        elif k < pi:
            # Искомый элемент в левой части
            high = pi - 1
        else:
            # Искомый элемент в правой части
            low = pi + 1

# Пример использования:
arr2 = [9, 3, 7, 1, 8, 2, 5]
k = 3  # 3-й наименьший элемент (нумерация с 0)
result = quick_select(arr2, k)
print(f"{k}-й наименьший элемент:", result)
