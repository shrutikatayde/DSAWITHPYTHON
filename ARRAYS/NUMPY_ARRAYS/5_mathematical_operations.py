import numpy as np
lst1 = list(map(int, input("Enter arr 1: ").split()))
lst2 = list(map(int, input("Enter arr 2: ").split()))

np_arr1 = np.array(lst1)
np_arr2 = np.array(lst2)

# <--------------ADDITION----------------->

addition = np.add(np_arr1, np_arr2)
print("addition: ", addition)

# <--------------SUBTRACTION----------------->

subtraction = np.subtract(np_arr1, np_arr2)
print("subtraction: ", subtraction)

# <--------------MULTIPLICATION----------------->

multiplication = np.multiply(np_arr1, np_arr2)
print("multiplication: ", multiplication)

# <--------------DIVISION----------------->

division = np.divide(np_arr1, np_arr2)
print("division: ", division)

# <--------------SQUARE ROOT----------------->

square_root_np_arr1 = np.sqrt(np_arr1)
print("square root np array 1: ", square_root_np_arr1)

square_root_np_arr2 = np.sqrt(np_arr2)
print("square root np array 2: ", square_root_np_arr2)

# <--------------TRANSPOSE----------------->

transpose = np.transpose([np_arr1, np_arr2])
print("transpose: ", transpose)