import numpy as np
lst = list(map(int, input().split()))
np_arr = np.array(lst)

ele_to_search = int(input("which element u want ro search: "))
search_res = np.where(np_arr == ele_to_search)
print("index:", search_res)

print("element:", np_arr[search_res])
