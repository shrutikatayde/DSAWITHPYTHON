import array as array
n = int(input())
lst = list(map(int, input().split()[:n]))
arr = array.array('i', lst)
# for i in range(n):
#     x = int(input())
#     arr.append(x)

arr = arr[::-1]  # ---> reversing
# arr[0:5]---> 1st 5 element
# arr[1:-1]----> start to end
print(arr)

for i in range(len(arr)):
    print(arr[i], end="")


