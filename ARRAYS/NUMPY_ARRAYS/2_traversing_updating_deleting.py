import numpy as np

# taking input array of size n
n = int(input())
lst = list(map(int, input().split()[:n]))
np_arr = np.array(lst)


# <----------reading array or traversing array--------->
for i in range(n):
    print(np_arr[i], end=" ")
print()


# <---------------updating array--------------->
# through program
# arr[1] = 5

# through user
index = int(input("enter index which u have to update"))
ele = int(input(f"enter ele which u have to enter at index {index}"))
np_arr[index] = ele
print(np_arr)


# <---------------deleting element-------------->
del_index = int(input("enter thr index from which u have to delete the element : "))
np_arr = np.delete(np_arr, del_index)
print(np_arr)
