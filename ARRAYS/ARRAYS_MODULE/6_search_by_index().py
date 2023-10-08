import array as arr
n = int(input())
lst = list(map(int, input().split()[:n]))
arr = arr.array('i', lst)
# print(arr[1])

# <-----------------SEARCH BY INDEX()----------------->

# index = arr.index(int(input()))  # index of entered element
# ele = arr[index]  # corresponding element to index searched

ele_to_search = int(input())
index = arr.index(ele_to_search)  # index of entered element
print(f"Index: {index} :: Element: {ele_to_search}")
