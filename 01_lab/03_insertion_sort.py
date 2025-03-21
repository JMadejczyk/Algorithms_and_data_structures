import random
n = 10
arr = [round(random.random() * n) for _ in range(n)]
print(arr)
print("Insertion sort")

def insertion_sort(arr):
    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
        print(arr)
insertion_sort(arr)