#!/usr/bin/env python3
"""Module that defines np_elementwise"""

import numpy as np


def np_elementwise(mat1, mat2):
    """Performs element-wise operations between two matrices"""

    return (np.add(mat1, mat2),
            np.subtract(mat1, mat2),
            np.multiply(mat1, mat2),
            np.divide(mat1, mat2))
