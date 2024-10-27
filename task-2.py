def binary_search_with_bounds(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    # Якщо не знайдено точного збігу, повертаємо upper_bound
    return (iterations, upper_bound)

arr = [0.1, 0.5, 0.9, 1.3, 2.0, 2.7, 3.5, 4.1, 5.0]
target = 2.5

print(binary_search_with_bounds(arr, target))  # Виведе: (3, 2.0)
