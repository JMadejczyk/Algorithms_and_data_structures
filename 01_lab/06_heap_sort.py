import random
n = 10
arr = [round(random.random() * n) for _ in range(n)]
print(arr)
print("Heap sort")

def heap_sort(arr):
    create_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        help = arr[0]
        arr[0] = arr[i]
        arr[i] = help
        max_heapify(arr, 0, i)
        
def create_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, i, n)

def max_heapify(arr, i, heap_size):
    print(arr)
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        help = arr[i]
        arr[i] = arr[largest]
        arr[largest] = help
        max_heapify(arr, largest, heap_size) 

heap_sort(arr)