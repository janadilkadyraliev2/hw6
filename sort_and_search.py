# Функция сортировки пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Функция бинарного поиска
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"Элемент {target} найден на индексе {mid}"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return f"Элемент {target} не найден в списке"

# Пример использования функций
if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    sorted_list = bubble_sort(unsorted_list)
    print("Отсортированный список:", sorted_list)

    # Поиск элемента в отсортированном списке
    element_to_find = 22
    search_result = binary_search(sorted_list, element_to_find)
    print(search_result)
