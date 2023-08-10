import numpy as np
from time import perf_counter
import math

def linear_search(arr, x, n):
    for index in range(n):
        if arr[index] == x:
            return index
    return -1

def binary_search(arr, x, n):
    low = 0
    high = n - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1


def fibmonaccian_search(arr, x, n):
 
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
 
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
 
    offset = -1
 
    while (fibM > 1):
 
        i = min(offset+fibMMm2, n-1)
 
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
 
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
 
        else:
            return i
 
    if(fibMMm1 and arr[n-1] == x):
        return n-1
 
    return -1


def performance(function, args, repeat=1):
    time = []
    for _ in range(repeat):
        start = perf_counter()
        r = function(*args)
        stop = perf_counter()
        time.append(stop - start)

    total = sum(time)
    med = total / len(time)
    print(f'Tempo total: {total}, tempo médio: {med}\n')