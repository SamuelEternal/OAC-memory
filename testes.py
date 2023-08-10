import numpy as np
from Seekers import linear_search, \
                    binary_search, \
                    fibmonaccian_search, \
                    performance


desired_mb_primary = 10
desired_mb_secondary = 10
repeat = 100
search_argorithms = (
        ('Linear Search', linear_search),
        ('Binary Search', binary_search),
        ('Fibonacci Search', fibmonaccian_search)
    )


num_elements = (desired_mb_primary * 1024 * 1024) // 8  # 64-bit integer
arr = np.arange(num_elements, dtype=np.uint64)
print(f'\nTamanho da lista: {arr.nbytes} bytes\nLength: {len(arr)}\n')

for name, function in search_argorithms:
    print(f'\n{name}:')
    performance(function, (arr, -1, len(arr)), repeat=repeat)

path = 'C:/Users/eletr/OneDrive/Documents/data/data.npy'

num_elements = (desired_mb_secondary * 1024 * 1024) // 8  # 64-bit integer
arr = np.arange(num_elements, dtype=np.uint64)
np.save(path, arr)
print(f'\nTamanho da lisa: {arr.nbytes} bytes\nLength: {len(arr)}\nSaved to {path}\n')

mmap = np.load(path, mmap_mode='r')
for name, function in search_argorithms:
    print(f'\n{name}:')
    performance(function, (mmap, -1, len(mmap)), repeat=repeat)