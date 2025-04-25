'''Write a program to make the length of each element 15 of a given Numpy 
array and the 
string centred, left-justified, right-justified with paddings of _ 
(underscore).''' 
 
import numpy as np 
 
list = [] 
 
n = int(input("Enter the number of elements in array : ")) 
 
for i in range(1, n + 1): 
    x = input(f"Enter element number {i} : ") 
    list.append(x) 
 
arr = np.array(list) 
 
centered_arr = np.char.center(arr, 15, '_')  
left_justified_arr = np.char.ljust(arr, 15, '_')   
right_justified_arr = np.char.rjust(arr, 15, '_')   
 
print("Original Array:") 
print(arr) 
 
print("\nCentered Array:") 
print(centered_arr) 
 
print("\nLeft-Justified Array:") 
print(left_justified_arr) 
 
print("\nRight-Justified Array:") 
print(right_justified_arr) 