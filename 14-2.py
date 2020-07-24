import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])

#1
                
vec2 = (np.pi/4) * vec1

#2

vec2 = np.cos( vec2 )

#3

vec3 = vec1 + (2 * vec2)

#5

vec4 = vec1 * mat1[:, np.newaxis]

#6

mat1.transpose()

#7

np.linalg.det(mat1)

#8

mat1.trace()

#9

vec1.min()

#10

def func():
    return vec1.min()

#11

mat1.min()

#12

A=np.array([[17, 24, 1, 8, 15],
            [23, 5, 7, 14, 16],
            [ 4, 6, 13, 20, 22],
            [10, 12, 19, 21, 3],
            [11, 18, 25, 2, 9]])

    
np.sum(A,axis = 0)

np.sum(A,axis = 1)

np.sum(np.diag(A))

###methode np.fliplr ke dar khode tmarin be onvane jam zanandeye ghotre gheyre asli moarefi shode bood
###kole elemnt haye matrix ra jam mizad va pasokhe 325 midad, dar natije man az do methode zir estefade kardam,
###ham methode bala va ham in do methode pain ghotrha ra ba ham jam mizanad.

np.sum(np.trace(A))

np.sum(np.diagonal(A))

#13

M = np.random.rand(10,10)

