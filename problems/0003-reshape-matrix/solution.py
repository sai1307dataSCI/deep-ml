import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
  if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
      return []
  
  #Flatten the matrix 
  arr = np.array(a)
  return np.reshape(arr, new_shape)