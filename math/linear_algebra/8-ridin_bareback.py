#!/usr/bin/env python3
"""Module that defines mat_mul"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication"""

    # Check multiplication compatibility
    if len(mat1[0]) != len(mat2):
        return None

    # Result matrix dimensions: len(mat1) x len(mat2[0])
    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            value = 0
            for k in range(len(mat2)):
                value += mat1[i][k] * mat2[k][j]
            row.append(value)
        result.append(row)

    return result
