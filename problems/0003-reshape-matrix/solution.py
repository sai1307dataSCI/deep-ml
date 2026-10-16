import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
  if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
      return []
  
  #Flatten the matrix 
  flat_arr = []
  for i in range(len(a)):
      for j in range(len(a[0])):
          flat_arr.append(a[i][j]) 
  
  reshaped_matrix = []
  index = 0
  for i in range(new_shape[0]):
      row = []
      for j in range(new_shape[1]):
          row.append(flat_arr[index])
          index+=1
      reshaped_matrix.append(row)
  
  return reshaped_matrix
print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (4, 2)))