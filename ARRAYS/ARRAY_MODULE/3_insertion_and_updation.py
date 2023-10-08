import array as arr

n = int(input())

# -----for taking input array in one line -------------
# lst = list(map(int, input().split()[:n]))
# print(lst)
# arrr = arr.array('i', lst)
# -----------------------------------------------------

arr = arr.array('i', [])

for i in range(n):
    arr_ele = int(input(f"Enter {i}th elements in array :"))
    arr.append(arr_ele)


print("Original Array--->", end=" ")
for i in range(n):
    print(arr[i], end=" ")
print()
print()


# <----------------------------INSERTION--> insert()--------------------------->
print("<---INSERTION--->")

# # ----adding element in array through program------
# arrr.insert(1, 3)   # ---> insert ele at given index
# arrr.append(15)     # ---> add ele at last position

# --------adding element in array by user------------
i_index = int(input("enter index at which u have to insert ele: "))
v_element = int(input(f"enter element u have to insert at index {i_index}: "))
arr.insert(i_index, v_element)

# ------printing updated array after insertion -------
m = len(arr)
print("After insertion--->", end=" ")
for i in range(m):
    print(arr[i], end=" ")
print()
print()

# <--------------------------UPDATING ARRAY ELEMENT ------------------>
print("<---UPDATION--->")

upd_index = int(input("enter index of ele which u have to change or update: "))
# gives index out of range error if we choose index which not in array or (index >= size of array)

upd_ele = int(input("enter new element which u have to put on that index "))
arr[upd_index] = upd_ele
print("After updation--->", end=" ")


for i in range(m):
    print(arr[i], end=" ")






