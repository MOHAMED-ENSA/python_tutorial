import numpy as np
from numpy.linalg import inv
#A = np.array([[1,9,3],[4,6,6],[7,-3,9]])
# print("A")
# print(A)
# Id = np.eye(3)
# Z = np.zeros((2,3,2) , dtype = 'int8')
# print(Z, Z.dtype)
# N = np.full((2,3) ,12, dtype='int8')
# print(N)
# M = np.full_like(A,3)
# print(M)
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
#C = np.array([[1,-1],[4,0],[1,5]]  , dtype='int16')
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

# 3D array  : 2 * 4 * 3
#X = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[1,3,3],[4,5,6],[7,8,9],[10,11,12]]])
#print(X.shape)
#print(X)
# X[1,0,1] = 2
# print(X)
# X[1,1,1:3] = 0
# print(X)
# random values :
# R = np.random.rand(4,3)
# print(R)
# RI = np.random.randint(0,10,size=(3,4))
# print(RI)
# be carefull when you copy 
# a = np.array([1,2,3])
# b = a.copy() 
# b[1] = -2 
# print(b) 
# print(a)
# math 
# M = np.cos(A)
# print(M)
# N =np.sin()
# N = np.tan()
# statistics 
S = np.array([[4,-4,3],[0,3,3],[1,5,-5]])
# print(np.max(S))
# print(np.min(S))
# print(np.mean(S))
# print(np.median(S))
# print(np.max(S , axis= 1))
# print(np.sum(S))
# print(np.sum(S, axis = 1))

# recognizing arrays 
# G = S.reshape(9,1) 
# print(G)
# AR = np.array([[1,2],[3,4],[5,6],[7,8]])
# ARR = AR.reshape(2,2,2)
# print(AR , AR.shape)
# print(ARR, ARR.shape)
# stck 
# A = np.ones((3,2), dtype = "int8")  
# B = np.zeros((3,2), dtype = "int8") 
# C = np.vstack((A,B))
# D = np.hstack((A,B))
# print("A = ",A , A.shape)
# print("B = ",B, B.shape) 
# print("C = ", C ,C.shape) 
# print("D = ",D, D.shape)

# loading data  
A = np.genfromtxt("data.txt" , delimiter = ',' ) 
A = A.astype('int8')# or we just can change the type 
print(A) 
# advanced indexing 
