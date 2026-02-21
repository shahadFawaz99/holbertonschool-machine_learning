#!/usr/bin/env python3
"""Module that defines np_cat"""


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis"""
    np = __import__('numpy')
    return np.concatenate((mat1, mat2), axis=axis)
