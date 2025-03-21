import random
import math
n = 10
arr = [round(random.random() * n) for _ in range(n)]
print(arr)
print("Merge sort")

def merge_sort(arr):
    if len(arr) > 1:
        mid = math.floor(len(arr)/2)
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)
    print(arr)
    return arr

def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    if len(a) > 0:
        c.append(a.pop())
    elif len(b) > 0:
        c.append(b.pop())
    return c

merge_sort(arr)