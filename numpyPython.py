import numpy as np 
from numpy.linalg import inv 
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(A) 
# B = np.array([[1,5],[5,6],[9,-4]])
# print(np.dot(A,B))
# print()
I = inv(A) 
#print(I)
R = np.dot(A,I)
print(np.allclose(R,np.eye(3)))
print(np.eye(3))
print(A.shape)
print(np.linalg.det(A))