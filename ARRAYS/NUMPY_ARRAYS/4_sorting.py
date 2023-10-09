import numpy as np

n = int(input())
lst = list(map(int, input().split()[:n]))
np_array = np.array(lst)

np_array.sort()
# sort_np_arr = np.sort(np_array)
print(np_array)
# print(sort_np_arr)
