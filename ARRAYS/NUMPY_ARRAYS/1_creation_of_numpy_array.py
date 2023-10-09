import numpy as np
# np_arr = np.np_array([1, 2, 3, 4, 5])
# print(np_arr)

n = int(input())
lst = list(map(int, input().split()[:n]))
np_arr = np.array(lst)
print(np_arr)
for i in range(n):
    print(np_arr[i], end=" ")
print()


zeros = np.zeros((2, 2))
print(zeros)

ones = np.ones((2, 2))
print(ones)

const = np.full((2, 2), 5)
print(const)

ide = np.eye(4)
print(ide)

rand = np.random.random((2, 2))
print(rand)
