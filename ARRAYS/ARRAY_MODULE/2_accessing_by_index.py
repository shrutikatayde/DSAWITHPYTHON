import array as arr
# Accessing ele from array using index
lst = list(range(1, 100, 2))
arrr = arr.array('i', lst)

# print array
for i in range(0, len(arrr)):
    print(arrr[i], end=" ")
print()

# accessing ele at index "25"
print(arrr[25])
