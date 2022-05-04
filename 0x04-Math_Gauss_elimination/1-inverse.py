#!/usr/bin/env python

import numpy as np
gaussian_elimination = __import__('0-gaussian_elimination').gaussian_elimination

if __name__ == "__main__":

  # Difine inverse function
  def inverse(A):
    #add zeros to the matrix
    #np.shape give the number of elements of A
    B = np.zeros(np.shape(A))
    j = np.shape(B)
    i = 0
    for i in range (0, j):
      #put 1 across the matrix
      #this create A'
      B[i][i] = 1
    inA = gaussian_elimination(A, B)
    return inA


  A = np.zeros((4, 4))
  A[2, 0]=1
  A[0, 1] = 1
  A[1, 3] =1
  A[3, 2] = 1
  print("The matrix A:\n",A)
  print("The inverse of the matrix A:\n",inverse(A))
  print("The identity matrix (The matrix A x The inverse of the matrix A): \n",A @ inverse(A) )