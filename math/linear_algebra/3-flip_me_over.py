#!/usr/bin/env python3
"""Module that defines matrix_transpose"""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix as a new matrix"""
    return [list(row) for row in zip(*matrix)]
