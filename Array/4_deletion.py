import array as arr
n = int(input())

arr = arr.array('i', [])

for i in range(n):
    arr_ele = int(input(f"Enter {i}th elements in array :"))
    arr.append(arr_ele)

del_index = int(input("enter index num from which u want to delete element: "))
arr.pop(del_index)

# # using remove() method
# arr.remove(del_index)

print("After deletion--->", end=" ")

for i in range(len(arr)):
    print(arr[i], end=" ")
