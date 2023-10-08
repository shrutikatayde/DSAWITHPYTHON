# Python Array Module
import array as arr

n1, n2, n3 = map(int, input("Enter size of array 1, array 2, and array 3 : ").split())

#  CREATION OF ARRAY
arr1 = arr.array('i', [])  # int array
arr2 = arr.array('f', [])  # float num array
arr3 = arr.array('u', [])  # unicode array

for i in range(n1):
    arr1_ele = int(input(f"Enter {i}th elements in array 1 :"))
    arr1.append(arr1_ele)
print()

for i in range(n2):
    arr2_ele = float(input(f"Enter {i}th elements in array 2 : "))
    arr2.append(arr2_ele)
print()

for i in range(n3):
    arr3_ele = input(f"Enter {i}th elements in array 3 : ")
    arr3.append(arr3_ele)
print()

# ------------------------------------------------
# ----------if the value of n1 = n2 = n3 = n------
# for i in range(n1):
#     arr1.append(int(input()))
#     arr2.append(float(input()))
#     arr3.append(input())
# ------------------------------------------------

# -----------print typecode--------------
# print(arr1.typecode)
# print(arr2.typecode)
# print(arr3.typecode)


# ----------print array------------------
print(arr1)
print(arr2)
print(arr3)

# ----------print length of array------------------
print(len(arr1))
print(len(arr2))
print(len(arr3))


# TRAVERSING ARRAY
# ---------printing the elements of arrays----------
for i in range(0, len(arr1)):
    print(arr1[i], end=" ")
print()
for i in range(0, len(arr2)):
    print(arr2[i], end=" ")
print()
for i in range(0, len(arr3)):
    print(arr3[i], end=" ")













