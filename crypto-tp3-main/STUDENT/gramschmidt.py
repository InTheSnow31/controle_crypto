import numpy as np
from numpy import array

# v2, v1 array of dim 1
def pr_coeff(v2: array, v1: array):
    return np.dot(v2, v1) / np.dot(v1, v1)

# orthogonal projection of v2 on R.v1
def proj(v2: array, v1: array):
    return np.dot(pr_coeff(v2, v1), v1)

# X is an array of (line) vectors [b1,...,b_i,...,b_n] , b_i of dim m >= n
# returns the array of (line) vectors [b*1,...,b*_i,...,b*_n]
# these vectors are orthogonal and span the same R-vector space
# uses Gram-Schmidt algorithm
def gs(X):
    Y = []
    for i in range(len(X)):
        temp_vec = X[i]
        for inY in Y:
            proj_vec = proj(X[i], inY)
            # print "i =", i, ", projection vector =", proj_vec
            temp_vec = temp_vec - proj_vec
            # print "i =", i, ", temporary vector =", temp_vec
        new_vec = np.copy(temp_vec)
        Y.append(new_vec)
    # make the list Y into an array
    return array(Y)
