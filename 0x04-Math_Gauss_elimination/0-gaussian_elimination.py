#!/usr/bin/env python3

import numpy as np

def gaussian_elimination(A, b):
#numpy.linalg.solve to Solve a linear matrix equation
    try:
        return np.linalg.solve(A, b)
    except LinAlgError:
        print("You can't divide by zero!")