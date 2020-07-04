import numpy as np 
from numpy.linalg import inv 
A = np.array([[1,9,3],[4,6,6],[7,-3,9]])
# print("A")
# print(A) 
# Id = np.eye(3)
# print("identity")
# print(Id)
# B = np.array([[1,5],[5,6],[9,-4]])
# print("multiplication")
# print(np.dot(A,B))
# I = inv(A) # we must verify two condition : A is a square array , det(A) not null
# print("inverse ")
# print(I)
# R = np.dot(A,I)
# print("identity from multi of A and inv A")
# print(R)
# print("better verification")
# print(np.allclose(R,np.eye(3)))
# print("shape ")
# print(A.shape)
# print("determinant of A")
# print(np.linalg.det(A))
#print(" number of dimentions :" , np.ndim(A))
#print("type : " ,  A.dtype)
# we can specify the type of data in an array : 
C = np.array([[1,-1],[4,0],[1,5]]  , dtype='int16')
#print('type :' , C.dtype)
# print("size of array :" , C.size)
# print("nb of byte : " , C.nbytes) # nbytes = size * itemsize

# 1.get data : 
# a : get specified value 
#print(C[1,0])
# b : get specified row/column : 
#print(C[1, : ])
# c : get specified range from a row 
# print(A [1 , 1:3:1]) # from the second row get from second element to the fourth (not included)
# 2. change data 
# print("befor !" , C)
# C[1,1] = 5 
# print("after  : " , C)
# C[1 , :] = [1,-1]
# print(C)
# C[: , 1] = 2
# print(C)