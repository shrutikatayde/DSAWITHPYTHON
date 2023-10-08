import array as arr
n = int(input())
lst = list(map(int, input().split()[:n]))  # list
arr = arr.array('i', lst)  # list to array
sorted_arr = arr.tolist()  # array to list
print(sorted_arr)

sorted_arr.sort()
print(sorted_arr)

sorted_arr.sort(reverse=True)
print(sorted_arr)