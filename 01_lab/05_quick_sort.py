import random
n = 10
arr = [round(random.random() * n) for _ in range(n)]
print(arr)
print("Quick sort")

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    print(arr)
        
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            help = arr[i]
            arr[i] = arr[j]
            arr[j] = help
    help = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = help
    return i + 1

quick_sort(arr, 0, len(arr) - 1)
        