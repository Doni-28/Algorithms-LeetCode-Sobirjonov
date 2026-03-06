import random
import time
import matplotlib.pyplot as plt


# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# QuickSort (Lomuto Partition)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


# Генерация почти отсортированного массива

def generate_almost_sorted(n):
    arr = list(range(n))
    # меняем местами 5% элементов
    for _ in range(n // 20):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# Измерение времени

def measure_time(sort_function, arr, is_quick=False):
    runs = 5  # количество повторов
    total_time = 0
    for _ in range(runs):
        data = arr.copy()
        start = time.time()
        if is_quick:
            sort_function(data, 0, len(data) - 1)
        else:
            sort_function(data)
        end = time.time()
        total_time += end - start
    return total_time / runs


# Основная часть тестирования

sizes = [1000, 5000, 10000]  

bubble_times = []
quick_times = []

print("=== Почти отсортированные данные ===")

for n in sizes:
    arr = generate_almost_sorted(n)

    bubble_time = measure_time(bubble_sort, arr)
    quick_time = measure_time(quick_sort, arr, True)

    bubble_times.append(bubble_time)
    quick_times.append(quick_time)

    print(f"Размер: {n} | Bubble Sort: {bubble_time:.4f}s | QuickSort: {quick_time:.4f}s")


# Построение графика

plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(sizes, quick_times, marker='o', label='QuickSort (Lomuto)')

plt.xlabel("Размер массива")
plt.ylabel("Среднее время выполнения (сек)")
plt.title("Сравнение алгоритмов: Почти отсортированные данные")
plt.legend()
plt.grid(True)
plt.show()