# Бинарный поиск в отсортированном массиве

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) 
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13]
x = 13
print(f' index element: {binary_search(arr, x)}')
