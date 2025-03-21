import random
n = 10
arr = [round(random.random() * n) for _ in range(n)]
print(arr)
print("Selection sort")


def selection_sort(arr):
    for i in range(0, n):
        curr = arr[i]
        min = n
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_idx = j
    
        arr[i] = arr[min_idx]
        arr[min_idx] = curr
        print(arr)
