import random
n = 10
arr = [round(random.random() * n) for _ in range(n)]


def bubble_sort(arr):
    def isSorted(arr):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True

    while not isSorted(arr):
        for i in range(1, n):
            a = arr[i-1]
            b = arr[i]
            if a > b:
                arr[i-1] = b
                arr[i] = a
                print(arr)
print(arr)
print("Bubble sort")
bubble_sort(arr)